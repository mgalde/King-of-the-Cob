from django.db import models, migrations
from django.contrib.auth.models import AbstractUser

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

# This defines the User types and assignes them to the propper user format. This replaces Django User model and the settings need to reflect this
class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_scrumaster = models.BooleanField(default=False)

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.body)
