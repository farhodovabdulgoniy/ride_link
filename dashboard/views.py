from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet

from driver.models import Driver, CarModel
from driver.serializers import DriverSerializer, CarModelSerializer

from passenger.models import Passenger
from passenger.serializers import PassengerSerializer

from ride.models import Ride, Booking
from ride.serializers import RideSerializer, BookingSerializer

from routeline.models import RouteLine
from routeline.serializers import RouteLineSerializer

from tariff.models import Tariff, DriverTariff
from tariff.serializers import TariffSerializer, DriverTariffSerializer


class RouteLineViewSet(ModelViewSet):
    queryset = RouteLine.objects.all()
    serializer_class = RouteLineSerializer
    permission_classes = [IsAdminUser]


class DriverListAPIView(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]


class DriverDetailAPIView(RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]


class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsAdminUser]


class TariffViewSet(ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAdminUser]


class DriverTariffViewSet(ModelViewSet):
    queryset = DriverTariff.objects.all()
    serializer_class = DriverTariffSerializer
    permission_classes = [IsAdminUser]


class PassengerListAPIView(ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAdminUser]


class PassengerDetailAPIView(RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAdminUser]


class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAdminUser]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]


