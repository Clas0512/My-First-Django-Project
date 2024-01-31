from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    email = forms.EmailField()