from rest_framework.serializers import ModelSerializer
from .models import Category, Product

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
