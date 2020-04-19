from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoriesViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
