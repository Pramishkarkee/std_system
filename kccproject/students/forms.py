from django import forms

class admin(forms.form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)