from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa: F401

from ..models import ToDoItem, ToDoList


class TodoModelTest(TestCase):
    """
    @classmethod
    def setUpTestData(cls):
        cls.todo = ToDoList.objects.create(title="First Todo")

    pass
    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(str(self.todo), "First Todo")
    """

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

    def test___str__(self):
        assert self.todolist.__str__() == self.todolist.title
        assert str(self.todolist) == self.todolist.title
        assert str(self.todoitem.title) == self.todoitem.title

    def test_todolist_content(self):
        self.assertEqual(f"{self.todolist.title}", "A good title")
        self.assertEqual(f"{self.todolist.owner}", "johndoe")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.todolist.get_absolute_url(), reverse("list", args=[self.todolist.id])
        )

    def test_todolist_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.post(
            reverse("list-add"),
            {
                "title": "New ToDo List",
                "owner": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDoList.objects.last().title, "New ToDo List")
        # self.assertEqual(ToDoList.objects.last().owner, {self.user.username})

    def test_listList_url_exists_at_desired_location(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_listview(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(reverse("list", args=[self.todolist.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ToDoList.objects.count(), 1)

    """
    def test_todoitem_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        form_data = {
            # "todo_list": self.todolist.id,
            "title": "A thing to do",
            "description": "Get this thing done",
        },
        request = self.client.post(
            reverse("item-add", args=[self.todolist.id]), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ToDoItem.objects.last().description, "Get this thing done")
    """
