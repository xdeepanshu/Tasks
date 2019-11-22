from django.db import models

class Task(models.Model):
    task_description = models.CharField(max_length = 100)
    finish_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_time = models.DateTimeField(auto_now=True, editable=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_description