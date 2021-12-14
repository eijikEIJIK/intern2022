from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    is_company = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    def __str__(self):
        return self.text

class WorkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resume = models.TextField()
