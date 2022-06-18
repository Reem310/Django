from django.shortcuts import render, HttpResponse, redirect
import random 	                

def index(request):
    if not 'counter' in request.session:
        request.session['counter']=0
    if not 'random' in request.session:
        request.session['random']=random.randint(1, 100)
    if not 'number' in request.session:
        request.session['number']=0
    print(request.session['random'])
    return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        request.session['counter']+=1
        request.session['number']=int(request.POST['number'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')




