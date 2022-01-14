from django.contrib import admin
from .models import Book, Student, Requested_Book

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Requested_Book)
