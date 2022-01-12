from django.contrib import admin
from .models import Book, Student
admin.site.register(Book)  # Let's the admin edit book's data
admin.site.register(Student)  # Let's the admin edit student's data
