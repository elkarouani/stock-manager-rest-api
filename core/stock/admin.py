from django.contrib import admin
from .models import Category, Product
from reversion.admin import VersionAdmin

admin.site.register(Product)

@admin.register(Category)
class ClientModelAdmin(VersionAdmin):
    pass

