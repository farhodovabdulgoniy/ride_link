from rest_framework import serializers

from .models import CarModel, Driver


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    car_model = CarModelSerializer(read_only=True)
    has_active_tariff = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = '__all__'

    def get_has_active_tariff(self, obj):
        return obj.has_active_tariff()


    # def validate(self, data):
    #     if data.get('is_active') and not data.get('is_paid_comission'):
    #         raise serializers.ValidationError("Водитель не может быть активным без оплаты комиссии.")
    #     return data
