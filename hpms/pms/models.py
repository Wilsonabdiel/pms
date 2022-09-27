from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.

class User(AbstractUser):
    pass

class Patient(models.Models):
    fullname = models.CharField(max_length=100)
    