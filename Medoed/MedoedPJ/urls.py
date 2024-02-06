from django.urls import path

from .views import *

urlpatterns = [
    path("index/", ProductClass.as_view(), name="info"),
    path("", BaseClass.as_view(), name= "Home"),
    path("add_prod/", ProdAddClass.as_view(), name= "add_prod"),
    path("contact/", ContactClass.as_view(), name= "contact"),
]