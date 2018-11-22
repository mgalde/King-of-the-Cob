from django.db import models, migrations
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

# Create your models here.

class Task(models.Model):
    """Model representing a Event or Task."""
    event = models.CharField(max_length=200, help_text='Enter a Task (e.g. Create Project)')
    points = models.IntegerField(help_text='Enter a Value between 1 to 100')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return '%s %s' % (self.task, self.points)

# This defines the User types and assignes them to the propper user format. This replaces Django User model and the settings need to reflect this
class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_scrumaster = models.BooleanField(default=False)

class Note(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a Title for the Note (e.g. ATTN Developers)')
    body = models.TextField(help_text='Enter your message here (e.g. Hello World, here I am!!)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.body)
