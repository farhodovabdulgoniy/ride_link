from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from driver.models import Driver
from driver.serializers import DriverSerializer

from routeline.models import RouteLine

from ride.models import Booking
from ride.serializers import BookingCreateSerializer


class DriverQueueAPIView(APIView):
    def get(self, request, *args, **kwargs):
        car_types = ['Start', 'Comfort', 'Lux']
        route_id = request.query_params.get("route_id")
        drivers_by_category = {}

        if not route_id:
            return Response({"error": "route_id is required"}, status=400)

        try:
            route = RouteLine.objects.get(id=route_id)
        except RouteLine.DoesNotExist:
            return Response({"error": "Invalid route_id"}, status=404)

        for car_type in car_types:
            drivers = Driver.objects.filter(
                car_model__car_type=car_type,
                is_active=True,
                ride__route=route
            ).order_by('-id')

            filtered_drivers = [driver for driver in drivers if driver.has_active_tariff()][:3]

            drivers_by_category[car_type] = DriverSerializer(filtered_drivers, many=True).data

        return Response(drivers_by_category)


class BookingCreateAPIView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer