from dataclasses import fields
from django.forms import ModelForm
from .models import Student


class NewStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["bits_id", "mobile_number", "room_no", "hostel"]
