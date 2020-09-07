from django.shortcuts import render
from rest_framework import viewsets
from todo_app import models, serializers

class TodoViewSet(viewsets.ModelViewSet):
    """
    Todo model Model viewset for CRUD Operation
    """
    serializer_class = serializers.TodoSerializer
    queryset = models.Todo.objects.all()
    