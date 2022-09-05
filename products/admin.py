from django.contrib import admin
from .models import Category, Manufacturer, Products

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Products)

