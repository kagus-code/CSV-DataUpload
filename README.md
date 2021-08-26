#  CSV data upload to Database

#### , 27/08/2021

#### By **Eston Kagwima**

## Description
This application allows a user to upload a csv file and the data from it is automatically uploaded to the database in the fastest and most efficient way



## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/CSV-DataUpload.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
- run:`pip install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=1
#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000


## Technologies Used

- Django 
- Python
- HTML
- Bootstrap
- Postgressql

## link to live site on heroku
https://datafull.herokuapp.com/


## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
