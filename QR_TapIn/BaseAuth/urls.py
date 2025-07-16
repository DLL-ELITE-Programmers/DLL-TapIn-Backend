from django.urls import path
from BaseAuth.views import main

urlpatterns = [
    path("", main)
]