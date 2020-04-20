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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        previous_product = instance.product
        previous_quantity = instance.command_quantity
        new_product = serializer.validated_data['product']
        new_quantity = serializer.validated_data['command_quantity']
        
        if previous_product == new_product :
            new_product.quantity -= (new_quantity - previous_quantity)
            new_product.save()
        else :
            previous_product.quantity += previous_quantity
            new_product.quantity -= new_quantity
            previous_product.save()
            new_product.save()

        serializer.save()
        return Response({'status': "The command is updated successfully"})


