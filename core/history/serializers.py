from rest_framework.serializers import ModelSerializer
from .models import history

class HistoriesSerializer(ModelSerializer):
    class Meta:
        model = history
        fields = '__all__'
