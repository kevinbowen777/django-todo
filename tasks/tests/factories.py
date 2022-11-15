import datetime

from accounts.tests.factories import UserFactory

import factory
import factory.fuzzy

import pytest

from ..models import ToDoList


@pytest.fixture
def todolist():
    return ToDoListFactory()


@pytest.fixture
def todoitem():
    return ToDoItemFactory()  # noqa: F821


class ToDoListFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="ToDo List ")
    date = factory.fuzzy.FuzzyDate(datetime.date(2022, 11, 11))
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = ToDoList


class ToDoItem(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="ToDo Item ")
    description = factory.fuzzy.FuzzyText(length=12, prefix="ToDo List ")
    # Is there any way in Factory boy to create a 'now' date?
    created_date = factory.fuzzy.FuzzyDate(datetime.date(2022, 11, 11))
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = ToDoList
