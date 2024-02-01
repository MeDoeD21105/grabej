from django.urls import path

from .views import *

urlpatterns = [
    path("", ProductClass.as_view())
]