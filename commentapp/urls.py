# from services import comment_service
from . import views
from django.urls import path

from .services import comment_service

app_name = "commentapp"

urlpatterns = [
    path('', views.comment_page, name='show_comments'),
    # path('')
    # path('', comment_service.get_comment_page, name='comments'),
]
