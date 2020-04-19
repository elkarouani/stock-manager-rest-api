from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    is_provider = serializers.BooleanField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['is_provider'] = self.validated_data.get('is_provider', '')
        return data_dict
