import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from pytest_django.asserts import (
    assertContains,
)

from ..models import ToDoItem, ToDoList
from ..views import (
    ItemDeleteView,
    ListDeleteView,
    ListListView,
)

# pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_list_list_view(rf, todolist):
    # Get the request
    request = rf.get(reverse("list", args=[todolist.id]))
    request.user = todolist.owner
    # Use the request to get the response
    response = ListListView.as_view()(request)
    # Test that the response is valid
    assert response.status_code == 200
    # assertContains(response, f"{todolist.owner}'s task lists")
    assertContains(response, f"{todolist.title}")
    assert ToDoList.objects.count(), 1


@pytest.mark.django_db
def test_todo_list_delete(rf, todolist):
    request = rf.post(
        reverse("list-delete", kwargs={"pk": todolist.id}),
    )
    request.user = todolist.owner
    callable_obj = ListDeleteView.as_view()
    response = callable_obj(request, pk=todolist.id)
    assert response.status_code == 302


"""
@pytest.mark.django_db
def test_todolist_create_view(rf, todolist, admin_user):
    form_data = {
            "title": "New ToDo List",
    }
    request = rf.post(reverse("list-add"), form_data)
    request.user = admin_user
    response = ListCreateView.as_view()(request)
    assert response.status_code, 302
    assert todolist.title, "New ToDo List"


@pytest.mark.django_db
def test_todo_item_create_view(rf, todoitem, todolist):
    form_data = {
        "todo_list": todolist.title,
        "title": "A thing to do",
        "description": "Get this thing done",
        "created_date": todoitem.created_date,
        "due_date": todoitem.due_date,
    }
    request = rf.post(
        reverse("item-add", args=[todolist.id]), form_data,
    )
    request.user = todolist.owner
    response = ItemCreateView.as_view()(request)
    assert response.status_code, 200
    # assert ToDoItem.objects.last().description, "Get this thing done"
"""


@pytest.mark.django_db
def test_todo_item_delete(rf, todoitem, todolist):
    request = rf.post(
        reverse(
            "item-delete",
            kwargs={
                "list_id": todolist.id,
                "pk": todoitem.id,
            },
        ),
    )
    request.user = todolist.owner
    callable_obj = ItemDeleteView.as_view()
    # response = callable_obj(request)
    response = callable_obj(request, list_id=todolist.id, pk=todoitem.id)
    assert response.status_code == 302


class TodoModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.todolist = ToDoList.objects.create(
            title="A good title",
            owner=self.user,
        )

        self.todoitem = ToDoItem.objects.create(
            todo_list=self.todolist,
            title="A good second title",
            description="Nice body content for a second article",
        )

    def test_listview(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("list", args=[self.todolist.id]))
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(ToDoList.objects.count(), 1)
