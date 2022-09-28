from django.contrib.auth.models import AbstractUser
from django.db import models
from tkinter import CASCADE



# Create your models here.

class User(AbstractUser):
    pass

class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    hedescrpt = models.CharField(max_length=1000)
    history = models.CharField(max_length=1000)
    diagnosis  = models.CharField(max_length=300)
    reason = models.CharField(max_length=1000)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    time = models.DateTimeField(auto_now_add=True)
    # isdischarged = models.BooleanField()
    # timedischarged = models.DateField()

