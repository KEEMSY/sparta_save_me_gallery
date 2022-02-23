from django.db import models

# Create your models here.
from project.models import BaseModel


class Activity(BaseModel):
    name = models.CharField(max_length=50)
    img = models.TextField()
    password = models.CharField(max_length=50)
