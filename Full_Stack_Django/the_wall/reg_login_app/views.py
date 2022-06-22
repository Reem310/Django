from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *


def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        errors = Users.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            conf_pwd=request.POST['conf_pwd']
            pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = Users.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                password=pwHash)
            newUser.save()
            request.session['userId'] = newUser.id
        return redirect('/success')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        error = Users.objects.login_validator(request.POST)
        if len(error) > 0:
            for key, value in error.items():
                messages.error(request, value)
            return redirect('/')
        else: 
            request.session['userId'] = Users.objects.get(email=request.POST['email']).id 
        return redirect("/success")

def success(request):
    if "userId" not in request.session:
        return redirect('/')
    context = {
        'loggedIn': Users.objects.get(id = request.session['userId'])
    }
    return redirect("/wall")

def destroy(request):
    del request.session['userId']
    return redirect('/')