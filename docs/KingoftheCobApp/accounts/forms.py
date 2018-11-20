from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.models import AbstractUser
from .models import User
from django.db import models, migrations
from django.utils.html import escape, mark_safe
from .models import User

# This defines how a developer is signed up
class DeveloperSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_developer = True
        if commit:
            user.save()
        return user

# This defines how a product owner is signed up
class OwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        return user

# This defines how a SCRUM master is signed up
class ScrumasterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_scrumaster = True
        if commit:
            user.save()
        return user
