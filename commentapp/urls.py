# from services import comment_service
from . import views
from django.urls import path

app_name = "commentapp"

urlpatterns = [
    path('', views.comment_page, name='show_comments'),
    path('delete', views.delete, name='delete'),
]
