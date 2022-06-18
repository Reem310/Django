from django.shortcuts import redirect, render, HttpResponse
from .models import *

def index(request):
    dojo = dojos.objects.all()
    context ={
        'dojos':dojo,
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == 'POST':
        if (request.POST['add'] == 'add_dojo'):
            newDojo = dojos.objects.create(
            name=request.POST['dojo_name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )
            newDojo.save()
        elif (request.POST['add'] == 'add_ninja'):
                newNinja = ninjas.objects.create(
                dojo = dojos.objects.get(id=int(request.POST['select_dojo'])),
                first_name = request.POST['fname'],
                last_name = request.POST['lname'],
            )
                newNinja.save()
    return redirect('/')