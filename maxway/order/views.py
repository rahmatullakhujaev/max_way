from django.shortcuts import render
import json
from urllib.parse import unquote
from maxway.product.models import Product
def cart(request):
    cart = request.COOKIES.get('cart')
    cart = unquote(cart)
    cart = json.loads(cart)
    products = Product.objects.filter(id__in=[item['id'] for item in cart])


    context = {
        'products' : products
    }
    return render(request, 'cart.html', context)

def order(request):
    return render(request, 'order.html')