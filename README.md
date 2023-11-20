# Ispani

## Overview
Ispani is a resume builder project, whereby a user can create a resume, update resume details and download the resume they created. THis project only allowes registered users  to create resumes, therefore if you are not a registered user you won't be able to create a resume in the platform.
The project is built using  Django 4, HTML 5, CSS 3, and Bootstrap 5 with a Bootswatch theme.
![Home Page](https://github.com/bhekumuzithabethe/django-resume-builder/blob/main/core/static/img/homepage.png)
## Prerequisites

1. [Python 3.8-3.12](https://www.python.org/)
This project uses Django v4.2.4. For Django to work, you must have a correct Python version installed on your machine. More information [Here](https://django.readthedocs.io/en/stable/faq/install.html)
1. [Visual Studio Code](https://code.visualstudio.com/)

## Installation

* Create a virtual environment.<br>
From the root directory, run:
>On macOS:
```
virtualenv venv
```
>On Windows:
```
python -m venv venv
```

* Activate the virtual environment.<br>
From the root directory, run: 
>On macOS:
```
source venv/bin/activate
```

>On Windows:
```
venv\scripts\activate
```

* Install required dependencies.<br>
From the root directory, run:
```
pip install requirements.txt
```

* Create an admin user to access the Django Admin interface.<br>
From the root directory, run:
```
python manage.py createsuperuser
```
When prompted, enter a username, email, and password.


## Run the application
From the root directory, run:
```
python manage.py runserver
```

## To view the application

Go to http://127.0.0.1:8000/. <br>
Once running you can create an account on the platform and make use of Ispani to create and download your resume.

## Copyright and License
Copyright © 2023 - current year Thabethe Programming. Code released under the MIT license.
