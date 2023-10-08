from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class UserSerializer(serializers.Serializer):
    """"
    Serializes a user object
    """
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data
        """
        user = User.objects.create_user(**validated_data)
        return user

class TaskSerializer(serializers.ModelSerializer):
    """ Serializes a task object"""
    user = UserSerializer(read_only=True)

    class Meta:
        """ Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'status']
