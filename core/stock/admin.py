from django.contrib import admin
from .models import Category, Product
from reversion.admin import VersionAdmin
import reversion

@admin.register(Category)
class CategoryModelAdmin(VersionAdmin):
    def log_change(self, request, object, message):
        print(dir(reversion))
        pass

    pass

@admin.register(Product)
class ProductModelAdmin(VersionAdmin):
    pass

