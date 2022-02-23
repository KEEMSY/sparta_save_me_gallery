from django.db import models
from project.models import BaseModel

# Create your models here.

class Comment(BaseModel):
    class Meta:
        db_table = "comment"

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.username