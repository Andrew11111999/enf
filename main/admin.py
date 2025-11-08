from django.contrib import admin
from .models import Category, Size, Product, \
    ProductImage, ProductSize


class ProductImageInline(admin.TabularInline):
    model = ProductImage(admin.TabularInline)
    extra = ProductImage
