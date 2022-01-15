from pydoc import visiblename
from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200, default="Not Available")
    isbn = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, default="Not Available")
    summary = models.CharField(max_length=200, default="Not Available")
    location = models.CharField(max_length=200, default="Not Available")
    availability = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + " [" + str(self.isbn) + "]"


HOSTEL_CHOICES = (
    ("Rana Pratap Bhawan", "Rana Pratap Bhawan"),
    ("Ashok Bhawan", "Ashok Bhawan"),
    ("Bhagirath Bhawan", "Bhagirath Bhawan"),
    ("Vishwakarma Bhawan", "Vishwakarma Bhawan"),
    ("Krishna Bhawan", "Krishna Bhawan"),
    ("Gandhi Bhawan", "Gandhi Bhawan"),
    ("Shankar Bhawan", "Shankar Bhawan"),
    ("Vyas Bhawan", "Vyas Bhawan"),
    ("Ram Bhawan", "Ram Bhawan"),
    ("Budh Bhawan", "Budh Bhawan"),
    ("Meera Bhawan", "Meera Bhawan"),
    ("NOT YET ALLOTED", "NOT YET ALLOTED"),
)


class Student(models.Model):
    BITS_ID = models.CharField(max_length=20, default="NOT YET UPDATED")
    # A unique no. generated for every user
    user_ID = models.IntegerField(default=-1)
    mobile_number = models.IntegerField(default=-1)
    room_no = models.IntegerField(default=-1)
    hostel = models.CharField(
        max_length=50, choices=HOSTEL_CHOICES, default="NOT YET ALLOTED"
    )

    def __str__(self):
        return f"[{self.BITS_ID}]"


class Requested_Book(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    issue = models.BooleanField(
        default=0
    )

    def get_absolute_url(self):
        return reverse("libmansys:user_home")

    def __str__(self):
        return str(self.book) + " " + str(self.student) + ""
