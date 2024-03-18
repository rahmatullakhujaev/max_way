from django.shortcuts import render
from .models import Category, Product
def index(request):
    categories = Category.objects.prefetch_related('product_set').all()
    print(categories)
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)