import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, column, Integer, String

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, SubmitField
from flask import Flask, render_template, jsonify, request, url_for, redirect
from database import get_jobs, load_job_from_db, insert_data_into_db , insert_data_user, redirect_user_login

app = Flask(__name__)

#jobs =[
   #     {"title": "Software Engineer", "location": "New York", "salary": "$90,000"},
    #    {"title": "Data Scientist", "location": "San Francisco", "salary": "$110,000"},
     #   {"title": "Product Manager", "location": "Seattle"},
     #   {"title": "Frontend Developer", "location": "Remote", "salary": "$150,000"}
    #]

#jobs = get_jobs()
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONNECTION_STRING")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initializing the database instance
db = SQLAlchemy()
db.init_app(app)

# Defining Database Tables
class User(db.Model):
  __tablename__ = 'users'
    
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=True, nullable=False)

#multiline commenst for the flask forms creation, as already craeted the forms in the html page of login and register.

'''class RegisterForm(FlaskForm):
    username=StringField('username', validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password=PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Password"})
    submit= SubmitField('Register')

    def validate_username(self, username):
        exusting_user= User.query.filter_by(username=username.data).first()
        if exusting_user:
            return ValidationError('Username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username=StringField('username', validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password=PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)], render_kw={"placeholder": "Password"})
    submit=SubmitField('Login')'''

   
@app.route("/")
def userlogin():
    return render_template('login_auth.html')

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
            data = request.form.to_dict()
            try:
                redirect_user_login(data)
                return  redirect(url_for('hello_world'))
            except ValueError as e:
                return redirect(url_for('show_error', message="Invalid username or password", title="Login Error", category="error"))
                
    return render_template('login.html')

@app.route('/error/<message>')
def show_error(message):
    return render_template('error.html', error_message=message)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form.to_dict()
        try:
            insert_data_user(data)
            return render_template('registered.html')
        except ValueError as e:
            return redirect(url_for('show_error', message="user already exists", title="Registration Error", category="error"))
    return render_template('register.html')

@app.route("/home")
def hello_world():
    jobs = get_jobs()
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    jobs = get_jobs()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    jobs=load_job_from_db(id)
   # return jsonify(jobs)
    if not jobs:
        return "Not Found", 404
    
    return render_template("job_id.html", job=jobs)

@app.route("/job/<id>/apply", methods=["POST"])
def apply_for_job(id):
    data=request.form.to_dict()
    insert_data_into_db(data, id)
    return render_template("application_submitted.html", application=data, job_id=id)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully on Aiven Cloud!")
    app.run(host="0.0.0.0", debug=True)
