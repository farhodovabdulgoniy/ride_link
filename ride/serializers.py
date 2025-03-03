from rest_framework import serializers

from .models import Booking, Ride

from tariff.models import DriverTariff


class BookingSerializer(serializers.ModelSerializer):
    payment_screenshot = serializers.ImageField(required=False, 
                                                allow_null=True)
    ride_id = serializers.PrimaryKeyRelatedField(
        queryset=Ride.objects.filter(is_completed=False), 
        write_only=True
    )

    class Meta:
        model = Booking
        fields = '__all__'


class RideSerializer(serializers.ModelSerializer):
    commission_payment_screenshot = serializers.ImageField(
        required=False, 
        allow_null=True
    )

    class Meta:
        model = Ride
        fields = '__all__'


class RideCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            'id', 
            'driver', 
            'route', 
            'commission_payment_screenshot', 
            'is_completed', 
            'bookings'
        ]

        extra_kwargs = {
            'commission_payment_screenshot': {'required': False},
            'bookings': {'read_only': True},
            'is_completed': {'read_only': True}
        }

    def validate(self, data):
        driver = data.get('driver')

        active_tariff = DriverTariff.objects.filter(driver=driver, is_paid=True). \
                                             order_by('-paid_at').first()
        if not active_tariff:
            raise serializers.ValidationError("Driver has no active tariff.")

        if Ride.objects.filter(driver=driver, is_completed=False).exists():
            raise serializers.ValidationError("Driver already has an active ride.")

        # completed_rides_count = Ride.objects.filter(driver=driver, is_completed=True).count()
        # if completed_rides_count >= active_tariff.selected_tariff.ride_limit:
        #     raise serializers.ValidationError("Ride limit for the current tariff has been reached.")
    
        return data


class BookingCreateSerializer(serializers.ModelSerializer):
    ride_id = serializers.PrimaryKeyRelatedField(
        queryset=Ride.objects.filter(is_completed=False), 
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id', 
            'passenger', 
            'ride_id',  
            'front_seat', 
            'extra_luggage', 
            'payment_type', 
            'payment_screenshot', 
            'is_cashback_used',
            'is_delivery',
            'cashback_used_percent',
        ]

        extra_kwargs = {
            'payment_screenshot': {'required': False},
            'is_cashback_used': {'required': False},
            'is_delivery': {'required': False},
            'cashback_used_percent': {'required': False},
        }

    def validate(self, data):
        passenger = data.get('passenger')
        ride = data.get('ride_id')
        is_cashback_used = data.get('is_cashback_used', False)
        front_seat = data.get('front_seat', False)
        is_delivery = data.get('is_delivery', False)
        cashback_used_percent = data.get('cashback_used_percent', 0)

        if ride.bookings.count() >= ride.driver.tariff.ride_limit:
            raise serializers.ValidationError("Ride booking limit for this tariff reached.")

        if not is_delivery and ride.bookings.filter(is_delivery=False).count() >= 4:
            raise serializers.ValidationError("Cannot book more than 4 passenger seats in a ride.")

        if front_seat and not is_delivery and ride.bookings.filter(front_seat=True, is_delivery=False).exists():
            raise serializers.ValidationError("Front seat is already taken.")

        if is_cashback_used:
            if passenger.cashback_percentage <= 0:
                raise serializers.ValidationError("Passenger does not have cashback available.")
            if cashback_used_percent > passenger.cashback_percentage:
                raise serializers.ValidationError("Cannot use more cashback than available.")

        return data

    def create(self, validated_data):
        ride = validated_data.pop('ride_id')
        passenger = validated_data['passenger']
        cashback_used_percent = validated_data.get('cashback_used_percent', 0)

        booking = Booking.objects.create(**validated_data)
        ride.bookings.add(booking)

        if validated_data.get('is_cashback_used'):
            passenger.cashback_percentage -= cashback_used_percent
            passenger.save(update_fields=['cashback_percentage'])

        return booking

