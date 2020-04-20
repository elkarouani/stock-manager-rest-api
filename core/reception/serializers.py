from rest_framework.serializers import ModelSerializer
from .models import Command

class CommandsSerializer(ModelSerializer):
    class Meta:
        model = Command
        exclude = ('created_at', 'updated_at', 'is_active',)
