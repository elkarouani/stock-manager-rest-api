from django.db import models
from stock.models import Product

class Command(models.Model):
    client_name = models.CharField(verbose_name="Client Name", max_length=100)
    client_cin = models.CharField(verbose_name="Client CIN", max_length=20)
    command_token = models.CharField(verbose_name="Command Token", max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    command_quantity = models.IntegerField(verbose_name="Requested Quantity")
    created_at = models.DateField(verbose_name="Created At", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Modified At", auto_now=True)
    is_active = models.BooleanField(verbose_name="Is Active ?", default=True)

    def __str__(self):
        return self.client_name + ': ' + self.product.title
