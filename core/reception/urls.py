from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommandsViewSet

router = DefaultRouter()
router.register(r'commands', CommandsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
