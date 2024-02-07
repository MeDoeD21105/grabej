from django.shortcuts import render
from .models import *
from .utils import *

from django.views.generic import ListView, DetailView

# Create your views here.



class ProductClass(DataMixin,ListView):
    model = Product
    template_name = "MedoedPJ/index.html"
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Product"
        return dict(list(context.items()) + list(c_def.items()))
    
class BaseClass(DataMixin, ListView):
    model = Product
    template_name = "MedoedPJ/base.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "baseClass"
        return dict(list(context.items()) + list(c_def.items()))

class ContactClass(DataMixin,ListView):
    model = Product
    template_name = "MedoedPJ/contact.html"
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Contact"
        return dict(list(context.items()) + list(c_def.items()))

class ProdAddClass(DataMixin,ListView):
    model = Product
    template_name = "MedoedPJ/add_prod.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "ProdAdd"
        return dict(list(context.items()) + list(c_def.items()))
    
class ShowPost(DataMixin, DetailView):
    model = Product
    template_name = "MedoedPJ/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = context["posts"].title
        return dict(list(context.items()) + list(c_def.items()))
    
    
        