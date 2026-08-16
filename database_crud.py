import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, column, Integer, String

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

load_dotenv()

app=Flask(__name__)
# 1. Replace with your actual Aiven connection details
  # Or your custom created database name

# 2. Build the Connection String with SSL enforcement
# Flask-SQLAlchemy uses 'mysql+pymysql://' format
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONNECTION_STRING")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize the database instance
db = SQLAlchemy()
db.init_app(app)

# 4. Define Database Models (Tables)
class User(db.Model):
  __tablename__ = 'users'
    
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return f'<User {self.username}>'

@app.route('/')
def index():
    try:
        # Simple test query using text()
        db.session.execute(text('SELECT 1'))
        return "Successfully connected to Aiven MySQL!"
    except Exception as e:
        return f"Connection failed: {str(e)}"

# 6. Initialize tables within application context
if __name__ == '__main__':
    with app.app_context():
        # db.create_all() creates tables defined in models that don't exist yet
        db.create_all() 
        print("Database tables created successfully on Aiven Cloud!")
        
    app.run(debug=True)
