from multiprocessing import Condition
from django.shortcuts import render, redirect
from .models import Book, Student
from .functions import is_new_user
from .forms import NewStudentForm


def user_home(request):
    # TODO:Check this view properly
    is_new_user(request)
    student = Student.objects.get(user_ID=request.user.id)
    if(request.method == 'POST'):
        s_form = NewStudentForm(request.POST, instance=student)
        if s_form.is_valid:
            s_form.save()
        return render(request, 'libmansys/user_home.html')
    elif(is_new_user):
        s_form = NewStudentForm(instance=student)
        context = {'s_form': s_form}
        return render(request, 'libmansys/update_user_profile.html', context)
    else:
        return render(request, 'libmansys/user_home.html')


def detail(request, ISBN):
    book = Book.objects.filter(isbn=ISBN)[0]
    context = {'book': book}
    return render(request, 'libmansys/book_detail.html', context)


def booklist(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'libmansys/book_list.html', context)
