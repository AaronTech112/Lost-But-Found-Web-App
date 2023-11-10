from django.shortcuts import render, HttpResponse, redirect
from . models import CustomUser, Item
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def dashboard(request):
    items = Item.objects.filter(status='missing')
    context = {'items':items}
    return render(request,"LbfApp/dashboard.html",context)

def report(request):
    return render(request,"LbfApp/report.html")

def profile(request):
    return render(request,"LbfApp/profile.html")

def login(request):
    return render(request,"LbfApp/login.html")

def register(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            form = RegisterForm()
            if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()
                    messages.info(request, "Account was create for " + form.cleaned_data.get('username'))
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error_message = "Invalid Credentials or Format" 
                    context = {"error_message":error_message}   

            context = {"form":form}  
            return render(request,"LbfApp/register.html",context)

def logout_user(request):
    logout(request)

def edit_profile(request):
    return render(request,"LbfApp/edit_profile.html")

def settings(request):
    return render(request,"LbfApp/settings.html")

