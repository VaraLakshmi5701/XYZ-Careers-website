# XYZ Careers Web Application

## Overview
This project is a Flask-based job portal website that allows users to register, log in, browse open jobs, and submit job applications. It is a simple full-stack web application that connects to a MySQL database hosted on Aiven.

## Application Purpose
The application is designed for a company or recruitment portal where:
- users can create an account
- users can sign in
- users can view job opportunities
- users can apply for jobs online
- job and applicant data is stored in a database

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- MySQL
- python-dotenv
- Bootstrap 5
- Jinja2 Templates

## Project Structure

- `app.py` - Main Flask application and routes
- `database.py` - Database helper functions for jobs, applications, and user login/register logic
- `database_crud.py` - Database connection / test script
- `templates/` - HTML templates for pages and UI
- `static/` - Static files such as CSS, images, and assets

## Main Features
- User registration
- User login
- Home page showing available jobs
- Job detail page
- Job application form
- Database-backed storage for users and applications
- JSON API endpoint for jobs

## How the Application Works

### 1. App Startup
When the app launches, it:
- loads environment variables from `.env`
- reads the database connection string from `DB_CONNECTION_STRING`
- initializes Flask and SQLAlchemy
- creates database tables if needed

### 2. User Registration
From the registration page:
- the user fills in username and password
- the form posts to `/register`
- the app collects the submitted data
- it checks validation rules
- it inserts the values into the `users` table

### 3. User Login
From the login page:
- the user submits username and password
- the app checks if the credentials match a user in the database
- if valid, the user is redirected to the home page
- if invalid, an error is shown

### 4. Viewing Jobs
The home page queries the database for all job listings:
- `SELECT * FROM jobs`
- the result is passed to the template
- job cards are rendered for each item

### 5. Applying for a Job
A user can open a specific job and submit an application form.
The app collects:
- name
- email
- education
- work experience
- resume URL
- job role

These values are inserted into the `applications` table.

## Database Notes
The app uses MySQL via SQLAlchemy connection strings and expects tables such as:
- `jobs`
- `users`
- `applications`

## Environment Variables
The app relies on a `.env` file with a variable named:

```env
DB_CONNECTION_STRING=mysql+pymysql://<username>:<password>@<host>:<port>/<database>?ssl=true
```

## Important Considerations
- Passwords should ideally be hashed before storing in the database
- The project is a simple learning/demo project and can be improved with:
  - better validation
  - user sessions
  - password hashing
  - admin dashboard
  - better error handling

## Files Summary

### app.py
Main Flask app containing routes and app configuration.

### database.py
Contains SQL queries and DB operations, including:
- `get_jobs()`
- `load_job_from_db(id)`
- `insert_data_into_db(data, id)`
- `insert_data_user(data)`
- `redirect_user_login(data)`

### database_crud.py
A separate script used to test database connectivity and table creation with SQLAlchemy.

### Templates
The HTML pages define the front end and use Bootstrap styling.

## License
This project is for educational/demo purposes.
