from rest_framework import serializers

from . models import RouteLine


class RouteLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteLine
        fields = '__all__'