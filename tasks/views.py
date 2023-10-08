from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints.
    GET tasks/ -> List tasks
    POST tasks/ -> Create a new task

    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        """Return the list of tasks for the currently authenticated user.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Save the post data when creating a new task."""
        serializer.save(user=self.request.user)
