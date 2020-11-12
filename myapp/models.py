from django.db import models


# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

