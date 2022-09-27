from django.shortcuts import render
from django.urls import reverse
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, request
from django.db import IntegrityError
# from .models import User
# Create your views here.

def index(request):
    return render(request, "pms/index.html")

def add(request):
    return render(request, "pms/add.html")

