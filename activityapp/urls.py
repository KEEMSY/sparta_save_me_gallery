from django.urls import path

from activityapp import views

app_name = "activityapp"

urlpatterns = [
    path("", views.choice_activity_page, name="choice"),
    path("image/", views.save_made_img, name="save_img"),
    path("choice/1", views.a_choice_activity_page, name="choice_1"),
    path("choice/2", views.b_choice_activity_page, name="choice_2"),
]
