from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    post = Product.objects.all()
    return render(request, "MedoedPJ/index.html",{"posts" : post})