from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import history
from stock.models import Product, Category
from .serializers import HistoriesSerializer

class HistoriesViewSet(ModelViewSet):
    queryset = history.objects.order_by('created_at')
    serializer_class = HistoriesSerializer
    
    @action(detail=True, methods=['get'])
    def redo_history(self, request, pk=None):
        history_instance = self.get_object()

        if history_instance.target == "Product" :
            if history_instance.action == "Create":
                Product.objects.get(title=history_instance.product_title).delete()

            if history_instance.action == "Update":
                pass
        pass
