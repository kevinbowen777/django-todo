from datetime import datetime as dt

import factory
import factory.fuzzy
from django.utils import timezone

# import pytest
from accounts.tests.factories import UserFactory

from ..models import ToDoItem, ToDoList


class ToDoListFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="ToDo List: ")
    # date = factory.fuzzy.FuzzyDate(datetime.date(2022, 11, 11))
    date = dt.now()
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = ToDoList


class ToDoItemFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="ToDo Item: ")
    description = factory.fuzzy.FuzzyText(length=12, prefix="Item to complete: ")
    # Is there any way in Factory boy to create a 'now' date?
    # created_date = factory.fuzzy.FuzzyDate(datetime.date(2022, 11, 11))
    # due_date = dt.now()
    created_date = dt.now()
    due_date = timezone.now() + timezone.timedelta(days=7)
    todo_list = factory.SubFactory(ToDoListFactory)

    class Meta:
        model = ToDoItem
