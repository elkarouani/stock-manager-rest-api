from django.db import models
import reversion

@reversion.register()
class Category(models.Model):
    title = models.CharField(verbose_name="Category title", max_length=50, unique=True)
    quantity = models.IntegerField(verbose_name="Category quantity", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

@reversion.register()
class Product(models.Model):
    title = models.CharField(verbose_name="Product title", max_length=100, unique=True)
    description = models.TextField(verbose_name="Product description")
    quantity = models.IntegerField(verbose_name="Product quantity")
    price = models.DecimalField(verbose_name="Product price", max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_run_out = models.BooleanField(verbose_name="Is the product run out of storage", default=False)

    def __str__(self):
        return self.title
