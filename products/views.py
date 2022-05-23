import os
from unicodedata import category
# from unicodedata import category
# from urllib import response
from django.conf import settings
from django.shortcuts import render

from products.models import Cart, Product
# from bloger.models import Article, Category, ImagesManager, Languages

print(settings.BASE_DIR)


def add_pro_to_car(request, product_id, quantity):
    pro = Product.objects.get(id=product_id)
    car_pro = Cart(product=pro, product_quantity=quantity)
    car_pro.save()
    return render(request, 'add_and_remove.html')


def remove_product(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return render(request, 'add_and_remove.html')


def cart(request):
    cart = Cart.objects.all()
    return render(request, 'cart.html', {"cart": cart})


def home_page(request):
    allProducts = Product.objects.order_by('create_at')
    return render(request, 'index.html',  {'products': allProducts})


def products(request):
    allProducts = Product.objects.order_by('-create_at')
    return render(request, 'products.html',  {'products': allProducts})


def productsWithCategory(request, product_category):
    allProducts = Product.objects.filter(cat=product_category)
    return render(request, 'products.html',  {'products': allProducts})


def single_product(request, product_id):
    my_product = Product.objects.get(id=product_id)
    my_products = Product.objects.filter(
        cat=my_product.cat).exclude(id=product_id)
    return render(request, 'single-product.html', {'single_product': my_product, "similar_products": my_products})
