from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HistoriesViewSet

router = DefaultRouter()
router.register(r'histories', HistoriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
