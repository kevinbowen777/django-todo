from django.views.generic import ListView
from .models import ToDoList


class ListListView(ListView):
    model = ToDoList
    template_name = "djangdo_app/index.html"
