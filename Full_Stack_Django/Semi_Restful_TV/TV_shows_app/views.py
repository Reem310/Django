
from django.shortcuts import render, HttpResponse,redirect
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
    if request.method == 'POST':
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