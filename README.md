# swe1-app

CS-GY 6063 SWE1: Django Hello World Developed and Deployed

http://swe1-app.us-west-2.elasticbeanstalk.com/

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

## create superuser

```bash
(.venv) $ python manage.py createsuperuser
```
create a superuser with username `admin` and password `admin` \
visit `localhost:8000/admin` to login to the admin site \
visit `localhost:8000/polls` to view the polls app

## export dependencies

```bash
(.venv) $ poetry export -f requirements.txt --output requirements.txt
```

## collect static files

```bash
(.venv) $ python manage.py collectstatic
```

### run the local server

```bash
(.venv) $ python manage.py runserver
```

## configure ebstalk

install [eb cli](https://github.com/aws/aws-elastic-beanstalk-cli-setup) \
```bash
$ eb init -p python-3.7 swe1-app --region us-west-2
$ eb create swe1-app
```

## deploy to ebstalk

```bash
$ eb deploy
```

## some useful ebstalk commands

```bash
# check the status of the environment
$ eb status
# open the console
$ eb console
# open the application in the browser
$ eb open
# view the logs
$ eb logs
# terminate the environment
$ eb terminate
```
