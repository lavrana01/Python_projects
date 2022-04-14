from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        
        password= forms.CharField(max_length=32, widget=forms.PasswordInput)
    