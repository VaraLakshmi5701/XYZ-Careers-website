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

  <img width="836" height="454" alt="image" src="https://github.com/user-attachments/assets/1b83949f-b2cf-4848-915c-160535318096" />
  <img width="470" height="400" alt="image" src="https://github.com/user-attachments/assets/6a72d430-a2f5-4fb2-b53f-3467e54b7ecf" />

<img width="680" height="284" alt="image" src="https://github.com/user-attachments/assets/334dc78d-64da-4d76-9639-604a9cdddad4" />


### 3. User Login
From the login page:
- the user submits username and password
- the app checks if the credentials match a user in the database
- if valid, the user is redirected to the home page
- if invalid, an error is shown

- <img width="593" height="399" alt="image" src="https://github.com/user-attachments/assets/307d68e4-1a90-4019-ab7f-e15ce75d20fd" />



### 4. Viewing Jobs
The home page queries the database for all job listings:
- `SELECT * FROM jobs`
- the result is passed to the template
- job cards are rendered for each item

<img width="556" height="495" alt="image" src="https://github.com/user-attachments/assets/3091cb13-af29-4691-8a94-928dd781b61f" />

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

<img width="748" height="442" alt="image" src="https://github.com/user-attachments/assets/c00bf26c-2f70-4d4d-9401-cd98740ae3f7" />

<img width="623" height="307" alt="image" src="https://github.com/user-attachments/assets/7f48b6b9-b88b-4846-9051-9ca0264e9c47" />

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

## Application working process:-
-----------------------------
"The Home button is used to return to the main jobs page after the user has logged in or navigated through the site."
"When the user clicks Home, the server loads the job listing page and displays the company banner, company description, and list of open positions."
"Each job card contains an Apply Now button. When clicked, it takes the user to the specific job page."
"This route looks up the selected job using load_job_from_db(id), checks whether the job exists, and renders the job detail page."
"On that job detail page, the user fills out the application form and submits it."
"The Contact Us button is a quick outreach link that opens a pre-filled email using mailto:."
"This button is meant for asking questions about the role, reporting an issue, contacting support, or requesting more information about hiring."
"The login form collects the username and password entered by the user."
"If the credentials are valid, the user is redirected to the home page. If invalid, an error is returned."
"The register page allows a new user to create an account."
"The submitted data goes to /register, where the app validates and then inserts it into the users table."
"If the username already exists, the app raises an error message."
"After successful registration, the app renders the registered.html page, which tells the user that their account was created successfully."
"The landing page at / is the first page users see. It provides two main actions: Login and Register."
"This acts as the entry point for authentication."


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
