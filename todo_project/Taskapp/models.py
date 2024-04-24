

# Create your models here.

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title
