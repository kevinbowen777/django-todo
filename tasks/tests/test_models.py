from accounts.tests.factories import UserFactory

from django.test import TestCase

from .factories import ToDoListFactory
from ..models import ToDoList  # noqa: F401


class ToDoListTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.todolist = ToDoListFactory()
        """
        self.review = ToDoList.objects.create(
            book=self.book,
            creator=self.user,
            review="An excellent review",
        )
        """

    def test__str__(self):
        assert self.todolist.__str__() == self.todolist.title
        assert str(self.todolist) == self.todolist.title

    def test_get_absolute_url(self):
        url = self.todolist.get_absolute_url()
        assert url == f"/list/{self.todolist.id}/"

    """
    def test_review__str__(self):
        assert self.review.__str__() == self.review.review
        assert str(self.review) == self.review.review

    def test_review_get_absolute_url(self):
        url = self.review.get_absolute_url()
        assert url == f'{"/books/"}'
    """
