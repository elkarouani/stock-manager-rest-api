from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from reversion.models import Version
from .models import Category, Product
from .serializers import CategoriesSerializer, ProductsSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

    @action(detail=True, methods=['get'])
    def undo_last_changes(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        version = Version.objects.get_for_object(category)[1]
        version.revision.revert()

        return Response({'status': "Last Changes reverted successfully"})

    @action(detail=False, methods=['get'])
    def recover_last_delete(self, request, pk=None):
        deleted_version = Version.objects.get_deleted(Category)[0]
        deleted_version.revision.revert()

        return Response({'status': "Last deleted category is recovered successfully"})

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category', 'is_run_out']
    search_fields = ['title']

    @action(detail=True, methods=['get'])
    def undo_last_changes(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        latest_product_version = Version.objects.get_for_object(product)[1]
        latest_product_version.revision.revert()

        return Response({'status': "Last changes reverted successfully"})

    @action(detail=False, methods=['get'])
    def recover_last_delete(self, request, pk=None):
        latest_deleted_version = Version.objects.get_deleted(Product)[0]
        latest_deleted_version.revision.revert()

        return Response({'status': "Last deleted product is recovered successfully"})

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance,
data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        validated_quantity = serializer.validated_data['quantity']
        serializer.validated_data['is_run_out'] = False if validated_quantity > 0 else True
        serializer.save()
        
        return Response({'status': "The product is updated successfully"})

    @action(detail=True, methods=['get'])
    def run_out(self, request, pk=None):
        product = self.get_object()
        product.is_run_out = True
        product.quantity = 0
        product.save()

        return Response({'status': "The product is run out of storage now !"})


