from django.db import models
from django.contrib.auth.models import User

class User(User):
    """Proxy model for the User model."""
    class Meta:
        """Meta class to map proxy model's fields with the base model's fields."""
        proxy = True

    def __str__(self):
        """Returns the username of the user."""
        return self.username

class Task(models.Model):
    """Model class for a task."""
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the title of the task."""
        return self.title
