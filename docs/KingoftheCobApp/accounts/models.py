from __future__ import unicode_literals
from django.db import models, migrations
from django.contrib.auth.models import AbstractUser
from django.core.validators import *
from django.utils.html import escape, mark_safe
import base64


# Create your models here.

# This will be used to develop the tasks for the api
class Task(models.Model):
    """Choice selection"""
    STATE_CHOICES = (
    ('unscheduled', 'unscheduled'),
    ('unstarted', 'unstarted'),
    ('started', 'started'),
    ('rejected', 'rejected'),
    ('finished', 'finished'),
    ('delivered', 'delivered'),
    ('accepted', 'accepted')
    )
    current_state = models.CharField(choices=STATE_CHOICES, max_length=20, default='unscheduled')
    event = models.CharField(max_length=100, help_text='Enter a Task (e.g. Create Project)')
    points = models.IntegerField(help_text='Enter a Value between 1 to 100', validators=[MaxValueValidator(100), MinValueValidator(1)])
    description = models.TextField(default='I need to enter something here', help_text='Explain the task here (e.g. This task will help me do X, Y and Z)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return '%s %s' % (self.event, self.description)

# This is more of a model for my models, a holdover from previous labs
class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype, self.timestamp, self.userid, self.requestor)


# This defines the User types and assignes them to the propper user format. This replaces Django User model and the settings need to reflect this
class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_scrumaster = models.BooleanField(default=False)

# This is used to create notes to the different teams
class Note(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a Title for the Note (e.g. ATTN Developers)')
    body = models.TextField(help_text='Enter your message here (e.g. Hello World, here I am!!)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.body)
