from django.urls import path, include
from . import views

urlpatterns = [
    path('branch', views.branch, name='branch')
]