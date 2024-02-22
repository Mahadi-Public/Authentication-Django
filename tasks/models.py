from django.db import models
from django.contrib.auth.models import User
from enu_helpers import CategoryChoices

# Create your models here.

class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='tasks_image/')
    category = models.CharField(max_length=7, choices=CategoryChoices)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    