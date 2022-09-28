from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, request
from django.db import IntegrityError
from .models import User, Patient
# Create your views here.

def index(request): 
    allPatients = Patient.objects.all().order_by('-time')
    return render(request, "pms/index.html",{
        "Patients":allPatients
    })

def all(request, id):
    allPatients = Patient.objects.get(pk=id)
    return render(request, "pms/all.html",{
         "patient":allPatients,
    })
    
def add(request):
    if request.method == "GET":
        allPatients = Patient.objects.all()
        return render(request, "pms/add.html",{
            "post":allPatients
        })
    else:    
        currentUser = request.user
        name = request.POST['name']
        age = request.POST['age']
        hd = request.POST['hd']
        history = request.POST['history']
        diagnosis = request.POST['diagnosis']
        reason = request.POST['reason']
        newPatient = Patient(
            doctor = currentUser,
            fullname = name,
            age = age,
            hedescrpt = hd,
            history = history,
            diagnosis = diagnosis,
            reason = reason 
        )
        newPatient.save()
        allPatients = Patient.objects.all()
        return HttpResponseRedirect(reverse("index"))
def edit(request):
    return

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "pms/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pms/register.html")
