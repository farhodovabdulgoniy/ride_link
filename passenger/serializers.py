from rest_framework import serializers

from .models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
        extra_kwargs = {
            "telegram_id": {
                "read_only": True
            }
        }