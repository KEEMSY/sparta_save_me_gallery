from . import views
from django.urls import path

app_name = "commentapp"

urlpatterns = [
    #테스트용 path!
    path('', views.get_comment_page, name='comments'),
]
