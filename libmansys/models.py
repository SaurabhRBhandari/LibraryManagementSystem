from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher=models.CharField(max_length=200,default='Not Available')
    isbn = models.PositiveIntegerField()
    genre = models.CharField(max_length=50,default='Not Available')
    summary = models.CharField(max_length=200,default='Not Available')
    location = models.CharField(max_length=200,default='Not Available')
    availability = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)
    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'