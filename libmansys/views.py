from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.generic import TemplateView
from .models import Book,Student
def index(request):
    student_list=Student.objects.all()
    student_id_list=[]
    for student in student_list:
        student_id_list.append(student.user_ID)
    current_user_id=request.user.id
    if current_user_id not in student_id_list:
        s=Student(user_ID=current_user_id)
        s.save()
        
    return render(request,'libmansys/home.html')

def detail(request, ISBN):
    book=Book.objects.filter(isbn=ISBN)[0]
    response=f'Name:{book.name} <br> Author:{book.author} <br> ISBN-10:{book.isbn} <br> Availibility:{book.availability}'
    return HttpResponse(response)

def booklist(request):
    book_list=Book.objects.all()
    output='<br>'.join([f'{b.name}|{b.author}|{b.isbn}|{b.publisher}' for b in book_list])
    return HttpResponse(output)