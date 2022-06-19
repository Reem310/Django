
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import *

def index(request):
    return redirect('/shows')

def all_shows(request):
    shows=Shows.objects.all()
    context={
        'shows':shows,
    }
    return render(request,'shows.html',context)

def new(request):
    return render(request,'add_show.html')

def add_show(request):
    if request.method == 'POST':
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/shows/new')
        
        else:
            add_show=Shows.objects.create(
                title=request.POST['title'], 
                network=request.POST['network'], 
                release_date=request.POST['rel_date'], 
                desc=request.POST['desc'])
            add_show.save()
    return redirect(f'/shows/{add_show.id}')

def show(request, _id):
    shows=Shows.objects.get(id=_id)
    context={
        'show':shows,
    }
    return render(request,'show_info.html',context)

def update(request,_id):
    shows=Shows.objects.get(id=_id)
    context={
        'show':shows,
    }
    return render(request,'edit_show.html',context)

def edit(request, _id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{_id}/edit')
        
    else:
        shows=Shows.objects.get(id=_id)
        shows.title=request.POST['title'] 
        shows.network=request.POST['network']
        shows.release_date=request.POST['rel_date']
        shows.desc=request.POST['desc']
        shows.save()
    return redirect(f'/shows/{_id}')
    

def destroy(request, _id):
    show = Shows.objects.get(id=_id)
    show.delete()
    return redirect('/shows')