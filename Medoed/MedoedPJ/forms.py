from django.forms import ModelForm
from .models import *

class Added_ProdForm(ModelForm):
    class Meta:
        model =  Product
        fields = ["title", "slug", "content", "photo", "price", "quantity", "sellerr"]