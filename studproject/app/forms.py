from django import forms
from .models import Student, Session

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'group']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['math', 'physics', 'programming']