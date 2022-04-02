from django.shortcuts import render
from .models import Category , Product , Review


# Create your views here.
def category(request):
    return render(request, 'products/category.html', {'category': Category.objects.all()})

def product(request):
    return render(request, 'products/product.html', {'product': Product.objects.all()})
    
def review(request):
    return render(request, 'products/review.html', {'review': Review.objects.all()})


def products(request):
    return render(request, 'products/products.html')
