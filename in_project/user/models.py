from django import forms
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.forms.widgets import PasswordInput



# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,null=False)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.first_name

class Post(models.Model):
    k = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField

    def __str__(self):
        return self.user
