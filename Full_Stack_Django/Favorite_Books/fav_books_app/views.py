from multiprocessing import context
from django.shortcuts import render, redirect
from reg_login_app.models import Users
from fav_books_app.models import Books
from django.contrib import messages


def books(request):
    if "userId" not in request.session:
        return redirect('/')
    context = {
        'loggedIn': Users.objects.get(id = request.session['userId']),
        'user': Users.objects.all(),
        'books': Books.objects.all(),
    }
    return render(request,'books.html',context)

def add_book(request):
    if request.method == 'POST':
        errors = Books.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
        else:
            user= Users.objects.get(id= request.session['userId'])
            newBook = Books.objects.create(
                title=request.POST['title'],
                description=request.POST['desc'],
                uploaded_by = user,
            )
            newBook.liked_books.add(user)
            newBook.save()
            messages.success(request, "Book is successfully added!")
        return redirect('/books')
    else:
        return redirect('/books')


def book_info(request,_id):
    book= Books.objects.get(id=_id)
    context={
        'loggedIn': Users.objects.get(id = request.session['userId']),
        'book':book,
        'user': Users.objects.all(),
    }
    return render(request, 'book_info.html',context)

def favorite(request, _id):
    user= Users.objects.get(id= request.session['userId'])
    like=Books.objects.get(id=_id)
    like.liked_books.add(user)
    return redirect(f'/books/{_id}')

def unfavorite(request,_id):
    user= Users.objects.get(id= request.session['userId'])
    like=Books.objects.get(id=_id)
    user.liked.remove(like)
    return redirect(f'/books/{_id}')

def update(request,_id):
    if request.method=='POST':
        errors = Books.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{_id}')
        else:
            book=Books.objects.get(id=_id)
            book.title=request.POST['title']
            book.description=request.POST['desc']
            book.save()
        return redirect(f'/books/{_id}')
    else:
        return redirect(f'/books/{_id}')

def delete(request,_id):
    book=Books.objects.get(id=_id)
    if request.session['userId'] == book.uploaded_by.id:
        book.delete()
    return redirect('/books')