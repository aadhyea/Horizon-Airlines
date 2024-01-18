from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request,'users/index.html')

    
def login_view(request):                            #comes from the login view
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request, "users/user_welcome.html")
        else:
             return render(request,"users/login.html",{
                 "message":"Invalid Credentials."
             })
    return render(request,"users/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message": "Passwords must match."
            })
       
        try:
            user = User.objects.create_user(username, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
        except:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request,"users/user_welcome.html")
    else:
        return render(request, "users/register.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"Logged Out Successfully!"
        })
