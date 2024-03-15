from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_TYPES = (
        ('grocery_shopping', 'Grocery Shopping'),
        ('medication_pickup', 'Medication Pickup'),
        ('companionship', 'Companionship'),
    )
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_type} task by {self.volunteer.username}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields related to user profile here

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
