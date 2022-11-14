from django.test import TestCase
from django.urls import reverse  # noqa: F401

from ..models import ToDoList


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = ToDoList.objects.create(title="First Todo")

    pass
    """
    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(str(self.todo), "First Todo")

    def test_listview(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    """
