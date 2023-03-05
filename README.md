# swe1-app

http://swe1-app.us-west-2.elasticbeanstalk.com/

[![Build Status](https://app.travis-ci.com/vchrombie/swe1-app.svg?branch=master)](https://app.travis-ci.com/vchrombie/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/vchrombie/swe1-app/badge.svg?branch=master)](https://coveralls.io/github/vchrombie/swe1-app?branch=master)

---
CS-GY 6063 SWE1: Personal Assignments

- Django Hello World Developed and Deployed

> Deploy working Simple Django application (https://docs.djangoproject.com/en/4.1/intro/tutorial01/) to individual AWS accounts.
> - Parts 1,2,3,4 of the tutorial need to be completed. This will produce a working polls application
> - Submit a URL of the working Django Application and a URL of the github repo.

- Travis CI

> Setup CI/CD and test suite for the Django Application
> - Configure Travis CI to run your build on push/pull requests to repository and deploy the app to AWS EB upon successful completion of the tests
> - Configure code formatting with [black](https://github.com/psf/black) and [flake8](https://flake8.pycqa.org/en/latest/) linter
> - Check test suite code coverage with [coverage.py](https://coverage.readthedocs.io/) & [coveralls](https://coveralls.io/) and add a badge to the `README.md`
> - Enable `Require status checks to pass before merging` on your repository
> - Submit your working Travis Dashboard Url.

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
(.venv) $ poetry export -f requirements.txt --output requirements-dev.txt --only dev
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

install [eb cli](https://github.com/aws/aws-elastic-beanstalk-cli-setup)
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

## run django tests

```bash
(.venv) $ python manage.py test
```

## install dev dependencies

```bash
(.venv) $ poetry add --group dev black flake8 coverage coveralls
```

## run black (code formatter)

```bash
(.venv) $ black --check .
```

## run flake8 (linter)

```bash
(.venv) $ flake8 .
```

## run coverage and coveralls

```bash
(.venv) $ coverage run --source='.' manage.py test
(.venv) $ coverage report
(.venv) $ coveralls
```

---

## References

- https://docs.djangoproject.com/en/3.2/intro/tutorial01/
- https://testdriven.io/blog/django-elastic-beanstalk/
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-getting-started.html
- https://docs.travis-ci.com/user/tutorial/
- https://black.readthedocs.io/en/stable/
- https://flake8.pycqa.org/en/5.0.4/
- https://coverage.readthedocs.io/en/6.5.0/
- https://coveralls-python.readthedocs.io/en/latest/
- https://docs.travis-ci.com/user/deployment/elasticbeanstalk/
