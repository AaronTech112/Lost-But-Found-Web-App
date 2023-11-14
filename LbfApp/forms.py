from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
           'profile_pic','username','fullname','email','phone_number','matric_number','gender','password1','password2'
            ]
        
class UpdateUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
           'username','fullname','email','phone_number','matric_number','gender','profile_pic',
            ]