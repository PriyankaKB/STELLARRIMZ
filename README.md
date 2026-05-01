# STELLARRIMZ
APIs for StellarRimz

## Create a Virtual Environment for the project
python -m venv .venv  

### Launch the virtual environment
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1     

## Pre-requisites:
Python 3.9 and higher
FastAPI
Django

## Install Dependencies:

pip install -r requirements.txt

## Change Directory
cd .\stellarrimz_api\myproject\

## Run the FastAPI
uvicorn myapp.fastapi:app --reload --port 8001

The application should start:

Go to URL: http://127.0.0.1:8001/api/data

The Hello message should appear as below.

![alt text](image-4.png)

In new terminal, run: 
python manage.py runserver

Below errors may appear:
"You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them."

If any errors are there run:
python manage.py migrate

Again restart the django server after the errors are fixed.

Django Server should start at http://127.0.0.1:8000/

![alt text](image-3.png)

Go to Interactive Demo:
Click "Say Hi!"

Stell-E will respond.
![alt text](image-2.png)





