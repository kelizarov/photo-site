from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PhotoUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Required email field")
    class Meta:
        model = PhotoUser
        fields = ['username', 'email','password1','password2',]
