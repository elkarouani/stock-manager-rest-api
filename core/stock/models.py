from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name="Category title", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    title = models.CharField(verbose_name="Product title", max_length=100)
    description = models.TextField(verbose_name="Product description")
    quantity = models.IntegerField(verbose_name="Product quantity")
    price = models.DecimalField(verbose_name="Product price", max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
