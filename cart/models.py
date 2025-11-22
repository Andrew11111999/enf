from django.db import models
from django.contrib.sessions.models import Session
from main.models import Product, ProductSize
from decimal import Decimal


class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart {self.session_key}'
