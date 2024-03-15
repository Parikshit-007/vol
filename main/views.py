from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# class TaskViewSet(viewsets.GenericViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     #permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(volunteer=self.request.user)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# views.py
from rest_framework import viewsets
from .models import Volunteer
from .serializers import VolunteerSerializer

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
