from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)

class Review(models.Model):
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,related_name='review',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='review',on_delete=models.CASCADE)



