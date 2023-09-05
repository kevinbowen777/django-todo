from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    path("list/add/", views.ListCreateView.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", views.ListDeleteView.as_view(), name="list-delete"),
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreateView.as_view(),
        name="item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdateView.as_view(),
        name="item-update",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDeleteView.as_view(),
        name="item-delete",
    ),
]
