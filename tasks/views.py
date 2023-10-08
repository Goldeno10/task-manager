from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .serializers import UserSerializer
from .permissions import IsSuperuserOrSelf
from rest_framework import permissions


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

# tasks/views.py

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for listing users."""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """Instantiates and returns the list of permissions that this view requires."""
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsSuperuserOrSelf]
        return [permission() for permission in permission_classes]
