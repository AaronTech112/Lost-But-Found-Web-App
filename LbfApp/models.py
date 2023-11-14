from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, )
    matric_number = models.CharField(unique=True,max_length=255)
    phone_number = models.IntegerField(null=True, unique=True)
    profile_pic = models.ImageField(default="avatar.png",upload_to = 'img', null = True,)
    GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather_not_say', 'Rather not say'),
    )
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES, default='rather_not_say')

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username']
 
    def __str__(self):
        return self.username
    
class Item(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    location_found = models.CharField(max_length=200 , blank=True)
    description = models.TextField(blank=True)
    contact = models.CharField(max_length=200,null= True)
    image = models.ImageField(upload_to='img', default = '',blank=True)
    STATUS = (
        ('retrieved','Retrieved'),
        ('missing','Missing'),
    )
    status = models.CharField(max_length=100, choices=STATUS, default='missing')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
