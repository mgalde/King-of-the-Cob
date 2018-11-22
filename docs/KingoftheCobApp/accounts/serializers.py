from rest_framework import serializers
from .models import Note, Task

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'url', 'title', 'body', 'created_at')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'url', 'event', 'points', 'description', 'created_at')
