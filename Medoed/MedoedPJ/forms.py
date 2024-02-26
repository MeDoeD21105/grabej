from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

class Added_ProdForm(ModelForm):
    class Meta:
        model =  Product
        fields = ["title", "slug", "content", "photo", "price", "quantity", "sellerr"]
        
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пороль")
    
    
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пороль")
    