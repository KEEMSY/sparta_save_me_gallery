# from services import comment_service
from django.urls import path

from . import views

app_name = "commentapp"

urlpatterns = [
    path("", views.comment_page, name="show_comments"),
    path("delete/", views.delete, name="delete"),
]
