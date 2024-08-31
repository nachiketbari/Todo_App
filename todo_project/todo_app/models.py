from django.db import models

# Create your models here.


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # The task title
    description = models.TextField(blank=True, null=True)  # Optional task description
    completed = models.BooleanField(default=False)  # Indicates if the task is completed
    created_at = models.DateTimeField(auto_now_add=True)  # The time when the task was created
    updated_at = models.DateTimeField(auto_now=True)  # The time when the task was last updated

    def __str__(self):
        return self.title  # String representation of the task (useful in admin interface)
