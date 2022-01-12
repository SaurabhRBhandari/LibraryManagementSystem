from django.db import models

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
