from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Category, Product
from .serializers import CategoriesSerializer, ProductsSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category', 'is_run_out']
    search_fields = ['title']

    @action(detail=True, methods=['get'])
    def run_out(self, request, pk=None):
        product = self.get_object()
        product.is_run_out = True
        product.quantity = 0
        product.save()
        return Response({'status': "The product is run out of storage now !"})


