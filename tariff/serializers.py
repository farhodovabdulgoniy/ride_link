from rest_framework import serializers

from . models import Tariff, DriverTariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class DriverTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverTariff
        fields = "__all__"

        extra_kwargs = {
            "created_at": {
                "read_only": True,
            },
            "updated_at": {
                "read_only": True
            }
        }