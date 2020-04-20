from rest_framework.viewsets import ModelViewSet
from .serializers import CommandsSerializer
from .models import Command

class CommandsViewSet(ModelViewSet):
    serializer_class = CommandsSerializer
    queryset = Command.objects.all()
