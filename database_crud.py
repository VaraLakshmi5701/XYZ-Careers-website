import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, column, Integer, String

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONNECTION_STRING")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

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
        db.session.execute(text('SELECT 1'))
        return "Successfully connected to Aiven MySQL!"
    except Exception as e:
        return f"Connection failed: {str(e)}"


if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
        print("Database tables created successfully on Aiven Cloud!")
        
    app.run(debug=True)
