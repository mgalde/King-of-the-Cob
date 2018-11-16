from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import date
from django.utils.html import escape, mark_safe

# Create your models here.

class Task(models.Model):
    """Model representing a Event or Task."""
    name = models.CharField(max_length=200, help_text='Enter a Task (e.g. Create Project)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Points(models.Model):
    """Model representing a point to a Task."""
    name = models.IntegerField(help_text='Enter a Value between 1 to 100')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
