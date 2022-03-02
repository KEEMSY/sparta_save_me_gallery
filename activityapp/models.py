from django.db import models

# Create your models here.
from project.models import BaseModel


class Activity(BaseModel):
    class Meta:
        db_table = "activity"

    model_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    img = models.TextField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Info(models.Model):
    class Meta:
        db_table = "info"

    model_name = models.CharField(max_length=128)
    model_img = models.URLField()
    example_img = models.URLField()
