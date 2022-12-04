# DJANGO TASK MANAGEMENT SYSTEM WITH REGISTRATION EMAIL FUNCTIONALITY

## Project Description

#### Task Management System was built with Django, PostgreSQL, Ajax & the Django REST FRAMEWORK. Feel free to make changes based on your requirements.

`And if you like this project, ADD a STAR ⭐️ to this project 👆`

----> Create a virtual environment:

```
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
```

----> Activate the virtual environment:

```
source envname/bin/activate
```

----> Clone this project

```
git clone https://github.com/DavidDanso/todo-api.git
```

----> Enter Project

```
cd projectName
```

## How to connect Project to PostgreSQL database

#### 1. Download PostgreSQL [ https://www.postgresql.org ]

#### 2. Download pgAdmin [ https://www.pgadmin.org ]

#### 3. Enter master password in pgAdmin [ one you created when download postgre ]

#### 4. Create a new server and connect to your Project

#### 5. Enter server name, hostname, port and password [ same password ]

#### 6. Create a new DB

#### 7. Use the name, username, password, host and port details to connect project to Postgre in the settings.py file

#### 8. Open terminal and install psycopg2

```
For Mac users run python3 manage.py migrate

For Windows users run python manage.py migrate
```

#### 10. Open pgAdmin, click on your server, scroll to schemas and refresh tables to view migrated data

## Running the App

----> To run the App, we use:

```
python3 manage.py runserver [ Command for Mac ]

python manage.py runserver [ Command for Windows ]
```

`⚠️ Then, the development server will be started at http://127.0.0.1:8000/`

## Login Credentials

----> Create Super User:

```
python3 manage.py createsuperuser[ Command for Mac ]

python manage.py createsuperuser [ Command for Windows ]
```

Then Add Email, Username and Password

## App Preview:

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Empty Feed
</p>
<img src="https://github.com/DavidDanso/todo-api/blob/main/static/images/UI/EMPTY.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Display Todo's
</p>
<img src="https://github.com/DavidDanso/todo-api/blob/main/static/images/UI/TODO.png" />
</td>
</table>

## Projects Enquiry

##### Email: davidkellybrownson@gmail.com

### Happy Coding!
