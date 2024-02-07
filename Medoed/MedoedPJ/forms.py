from django.forms import ModelForm
from .models import *

class Added_ProdForm(ModelForm):
    class Meta:
        model =  Product
        field = ["title", "content", "photo", "price", "quantit", "sellerr"]