from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from .models import ToDoItem, ToDoList


class ListListView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = "index.html"

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    paginate_by = 5


class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = "lists/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

    paginate_by = 5


class ListCreateView(LoginRequiredMixin, CreateView):
    model = ToDoList
    fields = ["title"]
    template_name = "lists/todolist_new.html"

    """
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    """

    def get_context_data(self):
        context = super(ListCreateView, self).get_context_data()
        context["title"] = "Add a new list"
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    template_name = "lists/todoitem_new.html"

    def get_initial(self):
        initial_data = super(ItemCreateView, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreateView, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    template_name = "lists/todoitem_new.html"

    def get_context_data(self):
        context = super(ItemUpdateView, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDoList
    template_name = "lists/todolist_confirm_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


# class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    template_name = "lists/todoitem_confirm_delete.html"

    """
    def test_func(self):
        obj = self.get_object()
        return obj.todo_list.owner == self.request.user
    """

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context
