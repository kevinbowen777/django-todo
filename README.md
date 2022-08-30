## Djangdo 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/djangdo.svg)](https://github.com/kevinbowen777/djangdo/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A simple todo application made using the Django web framework

---
## Features
 - Allow multiple users to logon, create, update and edit their own lists
 - Email account verifcation and support for GitHub Oauth login
 - Support for `django-debug-toolbar` in develpment

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
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

### Testing
 - `docker-compose exec web python manage.py test`

### Live Demo on Heroku:
 - [django-todo](https://kbowen-django-todo.herokuapp.com/)

---
## Screenshots

Home page
![Home Page](https://github.com/kevinbowen777/djangdo/blob/master/images/djangdo_home.png)

Add items
![Add items](https://github.com/kevinbowen777/djangdo/blob/master/images/djangdo_add_new_item.png)

List items
![List Items](https://github.com/kevinbowen777/djangdo/blob/master/images/djangdo_list_items.png)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/djangdo/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/djangdo/issues)
      to view currently open bug reports or open a new issue.
