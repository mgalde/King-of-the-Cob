from django.contrib import admin
from .models import User, Note, Task, Points

# Register your models here.
admin.site.register(User)

admin.site.register(Note)

admin.site.register(Task)

admin.site.register(Points)
