"""Sphinx configuration."""
project = "django-todo"
author = "Kevin Bowen"
copyright = f"2023, {author}"
#
html_theme = 'furo'
html_logo = 'django_24.png'
html_title = 'django-todo'
extensions = [
    'sphinx.ext.duration',
]
