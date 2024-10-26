from django.contrib import admin

from .models import Category, Product

admin.site.register(Category)  # register the Categorys model
admin.site.register(Product)  # register the Products model
