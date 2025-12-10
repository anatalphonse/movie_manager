from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout

# Create your views here.
def logout(request):
    authlogout(request)
    return redirect('login')


def login(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('list')
        else:
            error_message='invalid user'
    return render(request,'users/login.html',{'error_message':error_message})


def signup(request):
    user=None
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
            return redirect('login')
        except Exception as e :
            error_message=str(e) 
    return render(request,'users/create.html',{'user':user,'error_message':error_message})