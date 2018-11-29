from django.contrib import admin
from .models import User, Note, Task

# This registers what I want to see in the admin account. So I want to be able to manage the users, notes and tasks from a admin account
admin.site.register(User)

admin.site.register(Note)

admin.site.register(Task)
