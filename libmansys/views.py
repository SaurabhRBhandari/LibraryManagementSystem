from django.shortcuts import render
from .models import Book, Student,Requested_Book
from .functions import is_new_user
from .forms import NewStudentForm
from django.views.generic import ListView,CreateView

def user_home(request):
    is_new_user(request)
    return render(request, 'libmansys/user_home.html')


def detail(request, ISBN):
    book = Book.objects.filter(isbn=ISBN)[0]
    context = {'book': book}
    return render(request, 'libmansys/book_detail.html', context)

class BookListView(ListView):
    model=Book
    template_name='libmansys/book_list.html'
    context_object_name='book_list'
    ordering=['name']

class BookRequestView(CreateView):
    model=Requested_Book
    fields=['book']
    
    def form_valid(self,form):
        form.instance.student=Student.objects.get(
        user_ID=self.request.user.id)
        return super().form_valid(form)
    

def edit_profile(request):
    student = Student.objects.get(
        user_ID=request.user.id)  # getting the current user

    if(request.method == 'POST'):
        s_form = NewStudentForm(request.POST, instance=student)
        if s_form.is_valid:
            s_form.save()
        return render(request, 'libmansys/user_home.html')

    else:
        s_form = NewStudentForm(instance=student)
        context = {'s_form': s_form}
        return render(request, 'libmansys/update_user_profile.html', context)

