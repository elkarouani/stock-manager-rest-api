from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CommandsSerializer
from .models import Command
from stock.models import Product

class CommandsViewSet(ModelViewSet):
    serializer_class = CommandsSerializer
    queryset = Command.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_instance = serializer.validated_data['product']
        product_instance.quantity -= serializer.validated_data['command_quantity']
        product_instance.save()
        serializer.save()
        return Response({'status': "The command is successfully applied"})
