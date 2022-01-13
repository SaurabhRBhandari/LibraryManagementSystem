from django.shortcuts import render
from .models import Book
from .functions import is_new_user


def user_home(request):
    if(is_new_user(request)):
        return render(request, 'libmansys/new_user.html')
    else:
        return render(request, 'libmansys/user_home.html')


def detail(request, ISBN):
    book = Book.objects.filter(isbn=ISBN)[0]
    context={'book':book}
    return render(request, 'libmansys/book_detail.html',context)



def booklist(request):
    book_list = Book.objects.all()
    context={'book_list':book_list}
    return render(request,'libmansys/book_list.html',context)
