from django.urls import path, include
from . import views
urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('order', views.order, name='order')
]