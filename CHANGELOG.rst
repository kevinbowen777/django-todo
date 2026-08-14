.. _`changelog`:

=========
Changelog
=========

``django-todo`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-todo/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-todo 0.3.5 (2026-08-13)
==============================

Improved documentation
----------------------

-  (`#615 <https://github.com/kevinbowen777/django-todo/615>`_): Add towncrier 25.8.0.


New features
------------

-  (`#639 <https://github.com/kevinbowen777/django-todo/639>`_): Upgrade to Django 6.0.8

django-todo 0.3.4 (2026-07-27)
==============================

Contributor-facing changes
--------------------------

- : Add Python 3.14 support.

-  (`#633 <https://github.com/kevinbowen777/django-todo/633>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#635 <https://github.com/kevinbowen777/django-todo/635>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#629 <https://github.com/kevinbowen777/django-todo/629>`_): Drop support for Python 3.11.


New features
------------

-  (`#631 <https://github.com/kevinbowen777/django-todo/631>`_): Upgrade Django to 5.2.15.

django-todo 0.3.3 (2025-04-03)
==============================

Contributor-facing changes
--------------------------

-  (`#544 <https://github.com/kevinbowen777/django-todo/544>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#340 <https://github.com/kevinbowen777/django-todo/340>`_): Drop Python 3.10 support.


Improved documentation
----------------------

- : Update Sphinx to 8.2.3.


New features
------------

-  (`#545 <https://github.com/kevinbowen777/django-todo/545>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#548 <https://github.com/kevinbowen777/django-todo/548>`_): Replace safety package with pip-audit.

django-todo 0.3.2 (2025-01-15)
==============================

Contributor-facing changes
--------------------------

-  (`#479 <https://github.com/kevinbowen777/django-todo/479>`_): Add support for Python 3.13

-  (`#522 <https://github.com/kevinbowen777/django-todo/522>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#513 <https://github.com/kevinbowen777/django-todo/513>`_): Upgrade Django to 5.1.4

django-todo 0.3.0 (2023-12-30)
==============================

Contributor-facing changes
--------------------------

- : Upgrade Poetry to 1.7.1.

-  (`#210 <https://github.com/kevinbowen777/django-todo/210>`_): Migrate to non-root Docker user & venv.

-  (`#214 <https://github.com/kevinbowen777/django-todo/214>`_): Update Python to 3.12.0.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#362 <https://github.com/kevinbowen777/django-todo/362>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#386 <https://github.com/kevinbowen777/django-todo/386>`_): Upgrade to Django 5.0.

django-todo 0.2.0 (2023-05-12)
==============================

Contributor-facing changes
--------------------------

-  (`#246 <https://github.com/kevinbowen777/django-todo/246>`_): Install ruff. Drop flake8-* packages.

django-todo 0.1.0 (2023-05-08)
==============================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#219 <https://github.com/kevinbowen777/django-todo/219>`_): Add support for Python 3.12.

-  (`#225 <https://github.com/kevinbowen777/django-todo/225>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#230 <https://github.com/kevinbowen777/django-todo/230>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

-  (`#30 <https://github.com/kevinbowen777/django-todo/30>`_): Add Sphinx for documentation


New features
------------

-  (`#227 <https://github.com/kevinbowen777/django-todo/227>`_): Upgrade to Django 4.2.

django-todo 0.0.1 (2022-03-08)
==============================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.4


Miscellaneous internal changes
------------------------------

- : Initial commit
