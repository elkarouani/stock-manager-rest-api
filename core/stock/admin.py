from django.contrib import admin
from .models import Category, Product
from reversion.admin import VersionAdmin

@admin.register(Category)
class CategoryModelAdmin(VersionAdmin):
    pass

@admin.register(Product)
class ProductModelAdmin(VersionAdmin):
    pass

