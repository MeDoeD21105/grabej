from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, FormView, CreateView

from .models import *
from .utils import *
from .forms import *
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

class ProdAddClass(DataMixin, CreateView):
    form_class = Added_ProdForm
    template_name = "MedoedPJ/add_prod.html"
    success_url = reverse_lazy("Home")
    
    
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
    
    
class LoginUserr(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "MedoedPJ/login.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Авторизация"
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy("Home")
    
    
class RegisterUserr(DataMixin, CreateView):
    form_class =  RegisterUserForm
    template_name = "MedoedPJ/register.html"
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context["title"] = "Регистрация"
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self) -> str:
        return reverse_lazy("Home")