from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from ride.models import Ride
from ride.serializers import RideCreateSerializer

from driver.models import Driver


class RideCreateAPIView(CreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideCreateSerializer


class CompleteRideAPIView(APIView):
    def post(self, request):
        telegram_id = self.request.query_params.get('telegram_id', None)
        try:
            driver = Driver.objects.get(telegram_id=telegram_id)
            ride = Ride.objects.get(driver=driver, is_completed=False)
        except Driver.DoesNotExist:
            return Response({"error": "Driver not found."}, status=404)
        except Ride.DoesNotExist:
            return Response({"error": "Active ride not found."}, status=404)
        
        ride.is_completed = True
        ride.save()
        driver.is_active = False
        driver.save()

        return Response({"message": "Ride marked as completed."}, status=200)  