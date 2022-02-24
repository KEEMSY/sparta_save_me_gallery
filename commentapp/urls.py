# from services import comment_service
from . import views
from django.urls import path

from .services import comment_service

app_name = "commentapp"

urlpatterns = [
    #테스트용 path!
    path('', views.get_comment_page, name='comments'),
    # path('', comment_service.get_comment_page, name='comments'),
]
