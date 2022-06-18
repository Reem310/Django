from django.http import HttpResponse
from django.shortcuts import render,  redirect
import random
from datetime import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold']=0
    if not 'log' in request.session:
        request.session['log']=[]
    context={
            'gold':request.session['gold'],
            'log':request.session['log'],
        }
    return render(request, "index.html", context)


def game(request):
    if request.POST != {}:
        now = datetime.now()
        time= now.strftime('(%Y/%m/%d | %-I:%M %p)')
        if request.POST["place"]=='farm' or request.POST["place"]=='cave' or request.POST["place"]=='house':
            rand = random.randint(10, 20)
            request.session['log'].append(f"You entered a {request.POST['place']} and earned {rand} gold.{time}")
            
        else:
            rand=random.randint(-50, 50)
            if rand < 0:
                request.session['log'].append(f"You entered a {request.POST['place']} and lost {rand} gold.{time}")
            else: 
                request.session['log'].append(f"You entered a {request.POST['place']} and earned {rand} gold.{time}")
        request.session['gold'] += rand
        
    return redirect("/")


def destroy(request):
    request.session.clear()
    return redirect("/")