from rest_framework.viewsets import ModelViewSet
from .models import history
from .serializers import HistoriesSerializer

class HistoriesViewSet(ModelViewSet):
    queryset = history.objects.order_by('created_at')
    serializer_class = HistoriesSerializer
