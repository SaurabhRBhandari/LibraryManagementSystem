from django.shortcuts import render
from django.template import context
from .models import *
from .functions import is_new_user
from .forms import NewStudentForm
from django.views.generic import ListView, CreateView


def user_home(request):
    """Home page for a logged in user"""
    book_list = Book.objects.all()[:5]
    is_new_user(
        request)  # add a new user to the Student model,do nothing for an existing student
    student = Student.objects.get(user_ID=request.user.id)
    context = {"student": student, "book_list": book_list}
    return render(request, "libmansys/user_home.html", context)


def detail(request, ISBN):
    """Displays the detail of a given book"""
    book = Book.objects.filter(isbn=ISBN)[
        0
    ]  # Stores the book for which details are required

    context = {"book": book}
    return render(request, "libmansys/book_detail.html", context)


class BookListView(ListView):
    """Displays all books available at the library"""

    model = Book
    template_name = "libmansys/book_list.html"
    context_object_name = "book_list"
    ordering = ["name"]


class BookRequestView(CreateView):
    """To request a new book"""

    model = Requested_Book
    fields = ["book"]

    def form_valid(self, form):
        form.instance.student = Student.objects.get(
            user_ID=self.request.user.id)
        return super().form_valid(form)


def edit_profile(request):
    """To edit user profile"""
    student = Student.objects.get(
        user_ID=request.user.id
    )  # store's the current student

    if request.method == "POST":  # runs after the form is submitted
        s_form = NewStudentForm(request.POST, instance=student)
        if s_form.is_valid:
            s_form.save()
        # redirect user to home page
        return render(request, "libmansys/user_home.html")

    else:  # runs when the user wants to change its account details
        s_form = NewStudentForm(instance=student)
        context = {"s_form": s_form}
        return render(request, "libmansys/update_user_profile.html", context)


def pending_requests(request):
    """Displays all books requested by the student"""
    s = Student.objects.get(
        user_ID=request.user.id)  # getting the current user
    book_list = [request.book for request in Requested_Book.objects.filter(
        student=s, issue=False, reason="Provide a reason for rejection")]
    context = {"book_list": book_list}
    return render(request, "libmansys/pending_requests.html", context)


def issued_books(request):
    """Displays all books requested by the student"""
    s = Student.objects.get(
        user_ID=request.user.id)  # getting the current user
    book_list = [request.book for request in Requested_Book.objects.filter(
        student=s, issue=1)]
    context = {"book_list": book_list}
    return render(request, "libmansys/issued_books.html", context)
