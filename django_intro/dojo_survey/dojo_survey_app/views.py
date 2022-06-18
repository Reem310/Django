from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"index.html")

def result(request):
    print('got')
    u_name = request.POST['name']
    gender = request.POST['gender']
    location = request.POST['locations']
    language = request.POST['languages']
    u_comment = request.POST['comment']
    context = {
        "uname" : u_name,
        "gender" : gender,
        "language" : language,
        "ulocation" : location,
        "ucomment" : u_comment
    }
    return render(request,'result.html',context)