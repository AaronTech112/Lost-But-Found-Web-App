from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
           'username','fullname','email','phone_number','matric_number','gender','password1','password2'
            ]
