from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .functions import if_new_user

def user_home(request):
    if_new_user(request)
    return render(request,'libmansys/home.html')

def detail(request, ISBN):
    book=Book.objects.filter(isbn=ISBN)[0]
    response=f'Name:{book.name} <br> Author:{book.author} <br> ISBN-10:{book.isbn} <br> Availibility:{book.availability}'
    return HttpResponse(response)

def booklist(request):
    book_list=Book.objects.all()
    output='<br>'.join([f'{b.name}|{b.author}|{b.isbn}|{b.publisher}' for b in book_list])
    return HttpResponse(output)