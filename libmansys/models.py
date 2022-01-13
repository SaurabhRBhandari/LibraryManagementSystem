from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, default='Not Available')
    isbn = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, default='Not Available')
    summary = models.CharField(max_length=200, default='Not Available')
    location = models.CharField(max_length=200, default='Not Available')
    availability = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'


class Student(models.Model):
    BITS_ID = models.CharField(max_length=20, default='NOT YET UPDATED')
    # A unique no. generated for every user
    user_ID = models.IntegerField(default=-1)
    mobile_number = models.IntegerField(default=-1)
    room_no = models.IntegerField(default=-1)
    hostel = models.IntegerField(default=-1)  # index of college

    def __str__(self):
        return str(self.user_ID)
