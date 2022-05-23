from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=5000)
    price = models.FloatField(default=0)
    left_on_stock = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(
        Category, related_name='product_category', on_delete=models.CASCADE)
    product_thumnail = models.ImageField(upload_to='uploads/')
    product_cover_image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(default=1)
