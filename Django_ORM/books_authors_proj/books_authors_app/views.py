
from django.shortcuts import render, HttpResponse
from books_authors_app.models import *

def index(request):
    if request.method == 'POST':
        newBook = Book.objects.create(
            title=request.POST['book_title'],
            desc=request.POST['desc'],
    )
        newBook.save()
    books=Book.objects.all()
    context={
        "books":books,
    }
    return render(request, "index.html", context)

def books(request,_id):
    books=Book.objects.get(id=(_id))
    authors=Authors.objects.all()
    context={
        "books":books,
        "authors":authors,
    }
    if request.method == 'POST':
        author_selection = request.POST['select_author']
        books.authors.add(Authors.objects.get(id=author_selection))
    return render(request, "add_book.html", context)

def authors(request):
    if request.method == 'POST':
        newAuthor = Authors.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            notes=request.POST['note'],
    )
        newAuthor.save()
    authors=Authors.objects.all()
    context={
        "authors":authors,
    }
    return render(request, "add_author.html", context)

def new_author(request,_id):
    authors=Authors.objects.get(id=(_id))
    books=Book.objects.all()
    context={
        "books":books,
        "authors":authors,
    }
    if request.method == 'POST':
        book_selection = request.POST['select_book']
        authors.books.add(Book.objects.get(id=book_selection))
    return render(request, "authors.html", context)