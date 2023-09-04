import pytest
from django.test import RequestFactory

from accounts.tests.factories import UserFactory
from tasks.tests.factories import ToDoItemFactory, ToDoListFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def todolist():
    return ToDoListFactory()


@pytest.fixture
def todoitem():
    return ToDoItemFactory()
