from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Defines the admin interface for the Task model."""
    list_display = ['title', 'description', 'due_date', 'status', 'user']
