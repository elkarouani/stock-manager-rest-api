from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from reversion.models import Version
from .serializers import CommandsSerializer
from .models import Command
from stock.models import Product

class CommandsViewSet(ModelViewSet):
    serializer_class = CommandsSerializer
    queryset = Command.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['client_cin', 'command_token']

    @action(detail=True, methods=['get'])
    def undo_last_changes(self, request, pk=None):
        command = Command.objects.get(pk=pk)
        latest_command_version = Version.objects.get_for_object(command)[1]
        latest_command_version.revision.revert()

        product_requested = command.product
        latest_product_version = Version.objects.get_for_object(product_requested)[1]
        latest_product_version.revision.revert()

        return Response({'status': "Latest changes reverted successfully"})

    @action(detail=False, methods=['get'])
    def recover_last_delete(self, request, pk=None):
        latest_deleted_command = Version.objects.get_deleted(Command)[0]
        latest_deleted_command.revision.revert()

        return Response({'status': "Last deleted command is recovered successfully"})

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

    @action(detail=True, methods=['get'])
    def toggle_activation(self, request, pk=None):
        command_instance = self.get_object()
        command_instance.is_active = False if command_instance.is_active == True else True

        requested_product = command_instance.product
        requested_quantity = command_instance.command_quantity

        requested_product.quantity += requested_quantity if not command_instance.is_active else (requested_quantity * -1)

        requested_product.save()
        command_instance.save()

        activation_status = "activated" if command_instance.is_active else "deactivated"

        return Response({'status': "The command is successfully " + activation_status})


