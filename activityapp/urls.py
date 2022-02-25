from django.urls import path

from activityapp import views

app_name = "activityapp"

urlpatterns = [
    path("", views.upload_activity_page, name="choice"),
    path("image/", views.save_made_img, name="save_img"),
]
