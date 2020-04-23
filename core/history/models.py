from django.db import models
from stock.models import Category, Product
from reception.models import Command

class history(models.Model):
    action = models.CharField(verbose_name="History Action", max_length=100)
    target = models.CharField(verbose_name="History Target", max_length=50)
    category_id = models.IntegerField(verbose_name="Category Id")
    category_title = models.CharField(verbose_name="Category Title", max_length=50)
    product_id = models.IntegerField(verbose_name="Product Id")
    product_title = models.CharField(verbose_name="Product Title", max_length=100)
    product_description = models.TextField(verbose_name="Product Title")
    product_quantity = models.IntegerField(verbose_name="Product Quantity")
    product_price = models.DecimalField(verbose_name="Product Price", max_digits=8, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Product Category")
    product_is_run_out = models.BooleanField(verbose_name="Product is run out ?")
    command_id = models.IntegerField(verbose_name="Command Id")
    command_client_name = models.CharField(verbose_name="Command Client Name", max_length=100)
    command_client_cin = models.CharField(verbose_name="Command Client CIN", max_length=20)
    command_token = models.CharField(verbose_name="Command Title", max_length=10)
    command_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Command Title")
    command_quantity = models.IntegerField(verbose_name="Command Quantity")
    command_is_active = models.BooleanField(verbose_name="Command is active ?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[{}] : {} action on {}".format(self.created_at, self.action, self.target)
