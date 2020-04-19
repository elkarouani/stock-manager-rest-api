from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import CategoriesSerializer, ProductsSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
