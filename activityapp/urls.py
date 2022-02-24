from django.urls import path

from activityapp import views

app_name = "activityapp"

urlpatterns = [
    path('', views.upload_activity_page, name='home'),
    path('activities/image', views.upload_activity_page, name='upload'),
    path('activities/save/', views.save_made_img, name='save_img'),


]
