from rest_framework import serializers
from task.models import *

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    notes = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'

    def get_notes(self, obj):
        notes = obj.note_set.all()
        serializer = NoteSerializer(notes, many=True)
        return serializer.data

class ProfileSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = '__all__'

    def get_tasks(self, obj):
        tasks = obj.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data

    

