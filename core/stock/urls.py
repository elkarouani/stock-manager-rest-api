from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoriesViewSet, ProductsViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet)
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
