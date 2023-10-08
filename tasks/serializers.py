from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer as BaseCreateUserSerializer
from .models import Task



class CustomUserSerializer(UserSerializer):
    """
    Custom UserSerializer to add extra fields
    """
    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserCreateSerializer(BaseCreateUserSerializer):
    """
    Custom UserCreateSerializer to add extra fields
    """
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')


class TaskSerializer(serializers.ModelSerializer):
    """ Serializes a task object"""
    user = UserSerializer(read_only=True)

    class Meta:
        """ Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'status']
