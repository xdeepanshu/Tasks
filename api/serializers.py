from rest_framework import serializers
from tasks.models import Task

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id","task_description", "finish_time", "completed", "created_time", "hex_color")