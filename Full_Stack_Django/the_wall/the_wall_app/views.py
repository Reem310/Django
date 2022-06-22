from django.shortcuts import render, redirect
from reg_login_app.models import Users
from the_wall_app.models import Messages, comments

def wall(request):
    if "userId" not in request.session:
        return redirect('/')
    context = {
        'loggedIn': Users.objects.get(id = request.session['userId']),
        'user': Users.objects.all(),
        'msg': Messages.objects.all(),
        'comment': comments.objects.all()
    }
    return render(request,'wall.html',context)

def post_msg(request):
    if request.method == 'POST':
        new_msg = Messages.objects.create(
            messages = request.POST['msg'],
            user=Users.objects.get(id=request.session['userId']) ,
        )
        new_msg.save()
    return redirect('/wall')

def post_comment(request):
    if request.method == 'POST':
        new_comment = comments.objects.create(
            comment = request.POST['comment'],
            message = Messages.objects.get(id=request.POST['msg_id']),
            user=Users.objects.get(id=request.session['userId']) ,
        )
        new_comment.save()
    return redirect('/wall')

def delete_post(request,_id):
    delete = Messages.objects.get(id=_id)
    delete.delete()
    return redirect('/wall')