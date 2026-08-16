from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv

load_dotenv()
# Option 1: Using PyMySQL driver (Recommended for pure Python environments)
engine_pymysql = create_engine(
    os.getenv("DB_CONNECTION_STRING"),
    # echo=True
)

def get_jobs():
    # Verify the connection works
    with engine_pymysql.connect() as connection:
        pool_recycle=1800,  # Recycles connections older than 30 mins
        pool_pre_ping=True 
        result = connection.execute(text("SELECT * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):
    with engine_pymysql.connect() as conn:
        pool_recycle=1800,  # Recycles connections older than 30 mins
        pool_pre_ping=True 
        result=conn.execute(text("select * from jobs where id=:val"),
                            { "val": id })
        rows=result.all()
        if(len(rows)==0):
            return None
        else:
            return rows[0]._asdict()


def insert_data_into_db(data, id):
    with engine_pymysql.connect() as conn:
        result = conn.execute(text("SELECT title from jobs where id=:val"),
                            { "val": id })
        row=result.fetchone()
        conn.execute(text("INSERT INTO applications (name, email, linkedin_url, education, work_experience, resume_url, Job_role) VALUES (:name, :email, :linkedin_url, :education, :work_experience, :resume_url, :Job_role)"), 
                    {"name": data.get('name'), 
                     "email": data.get('email'),
                     "linkedin_url": data.get('linkedin_url', ''),
                     "education": data.get('education'),
                     "work_experience": data.get('work experience'),
                     "resume_url": data.get('resume_url'),
                     "Job_role": row[0]})
        conn.commit()


def user_exists_error(username):
    raise ValueError(f"The username '{username}' already exists. Please choose another one or log in.")


def insert_data_user(data):
    with engine_pymysql.connect() as conn:
        username = data.get('username', '').strip()
        password = data.get('password', '')

        if not username or not password:
            raise ValueError("Username and password are required")
        elif len(username) < 4 or len(password) < 6:
            raise ValueError("Username should be at least 4 characters and password should be at least 6 characters long")

        result = conn.execute(
            text("SELECT username FROM users WHERE username=:username"),
            {"username": username}
        )
        row = result.fetchall()

        if len(row) > 0:
            user_exists_error(username)

        conn.execute(
            text("INSERT INTO users (username, password) VALUES (:username, :password)"),
            {"username": username, "password": password}
        )
        conn.commit()

def redirect_user_login(data):
    with engine_pymysql.connect() as conn:
        username = data.get('username', '').strip()
        password = data.get('password', '')

        if not username or not password:
            raise ValueError("Username and password are required")
        elif len(username) < 4 or len(password) < 6:
            raise ValueError("Username should be at least 4 characters and password should be at least 6 characters long")

        result = conn.execute(
            text("SELECT username, password FROM users WHERE username=:username AND password=:password"),
            {"username": username, "password": password}
        )
        row = result.fetchall()

        if len(row) > 0:
            return True
        return False