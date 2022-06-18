from django.shortcuts import redirect, render, HttpResponse
from .models import *

def index(request):
    user = users.objects.all()
    context ={
        'users':user
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        newUser = users.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email_address=request.POST['email'],
            age=request.POST['age'],
        )
        newUser.save()
    return redirect('/')