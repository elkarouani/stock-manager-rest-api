from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategoriesSerializer

class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

