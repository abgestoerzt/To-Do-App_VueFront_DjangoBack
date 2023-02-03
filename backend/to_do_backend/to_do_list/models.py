from django.db import models

# Create your models here.


class ToDo(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
