from django.shortcuts import render

# Create your views here.

from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 