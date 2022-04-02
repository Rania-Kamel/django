from django.urls import path
from . import views

urlpatterns = [
    path('category' , views.category , name="category"),
    path('product' , views.product , name="product"),
    path('review' , views.review , name="review"),
    path('' , views.products , name="products"),
]