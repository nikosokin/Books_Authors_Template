from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    context = {
        "books" : Books.objects.all(),
    }
    return render(request, "books_authors_app/index.html", context)

def addBook(request):
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        

        Books.objects.create(title=title, desc = description)
    
    return redirect("/")

def addAuthor(request):

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        notes = request.POST['notes']
        
        Authors.objects.create(first_name=fn, last_name=ln, notes=notes)
    
    return redirect("/authors")

def showBook(request, num):

    context = {
        "currentBook" : Books.objects.get(id=num),
        "authors" : Authors.objects.all()
    }

    return render(request, "books_authors_app/showBook.html", context)

def authors(request):
    context = {
        "authors" : Authors.objects.all()
    }
    return render(request, "books_authors_app/author.html", context)

def showAuthor(request, num):

    context = {
        "currentAuthor" : Authors.objects.get(id=num),
        "books" : Books.objects.all()
    }

    return render(request, "books_authors_app/showAuthor.html", context)

def addAtoB(request):

    if request.method == "POST":
        book = request.POST['currentBook']
        author = request.POST['currentAuthor']
        
        updateBook = Books.objects.get(id=book)
        updateBook.author.add(author)

        return redirect('/')

def addBtoA(request):

    if request.method == "POST":
        book = request.POST['currentBook']
        author = request.POST['currentAuthor']

        updateAuthor = Authors.objects.get(id=author)
        updateAuthor.book.add(book)

    return redirect('/')