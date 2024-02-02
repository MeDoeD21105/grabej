from django.urls import path

from .views import *

urlpatterns = [
    path("index/", ProductClass.as_view()),
    path("", base),
]