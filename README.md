## django-todo 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django-todo.svg)](https://github.com/kevinbowen777/django-todo/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A simple todo application made using the Django web framework

##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - Allow multiple users to logon, create, update and edit their own lists
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - Basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generation
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage
     - For additional links to package resources used in this repository, see the [Package Index](docs/package_index.md)

---

### Installation
 - `git clone https://github.com/kevinbowen777/djangdo.git`
 - `cd djangdo`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker compose up --build`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

---

### Application Demo
A live application demonstration hosted at Heroku
 - [django-todo](https://kbowen-django-todo.herokuapp.com/)

---

### Screenshots

Home page
![Home Page](https://github.com/kevinbowen777/django-todo/blob/master/images/djangdo_home.png)

Add items
![Add items](https://github.com/kevinbowen777/django-todo/blob/master/images/djangdo_add_new_item.png)

List items
![List Items](https://github.com/kevinbowen777/django-todo/blob/master/images/djangdo_list_items.png)

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django-todo/issues)
      to view currently open bug reports or open a new issue.
