# swe1-app
CS-GY 6063 SWE1: Django Hello World Developed and Deployed

> Deploy working Simple Django application (https://docs.djangoproject.com/en/4.1/intro/tutorial01/) to individual AWS accounts.
> - Parts 1,2,3,4 of the tutorial need to be completed. This will produce a working polls application
> - Submit a URL of the working Django Application and a URL of the github repo.

---

## create a new django project

I used [poetry](https://python-poetry.org/) to setup, manage and install dependencies for the project.

```bash
$ poetry new swe1-app
$ cd swe1-app
$ poetry add django
$ poetry shell
(.venv) $ django-admin startproject swe1_app .
(.venv) $ python manage.py runserver
```

## create a polls app

```bash
(.venv) $ python manage.py startapp polls
```

## create polls model and migrations

```bash
(.venv) $ python manage.py makemigrations polls
(.venv) $ python manage.py migrate
```
