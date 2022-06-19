from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)


def add_course(request):
    if request.method == 'POST':
        errors = Courses.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            courses = Courses.objects.create(
                name=request.POST['name'],
                description=request.POST['desc'],
            )
            courses.save()
    return redirect('/')


def delete_option(request, _id):
    option = Courses.objects.get(id=_id)
    context = {
        'options': option,
    }
    return render(request, 'destroy.html', context)


def destroy(request, _id):
    remove = Courses.objects.get(id=_id)
    remove.delete()
    return redirect('/')
