from django.db import models
from base.models import TimestampedModel


class Booking(TimestampedModel):
    passenger = models.ForeignKey("passenger.Passenger", 
                             on_delete=models.CASCADE)

    front_seat = models.BooleanField(default=False)
    extra_luggage = models.TextField(blank=True, null=True)

    is_delivery = models.BooleanField(default=False)

    ride_price = models.DecimalField(max_digits=10, 
                                     decimal_places=2,
                                     blank=True,
                                     null=True)

    is_cashback_used = models.BooleanField(default=False)
    cashback_used_percent = models.PositiveIntegerField(default=0,
                                                        null=True,
                                                        blank=True)

    payment_type = models.CharField(max_length=10, 
        choices=[
            ('Cash', 'Cash'), 
            ('Card', 'Card'), 
        ]
    )

    payment_screenshot = models.ImageField(
        null=True,
        blank=True,
        upload_to='passengers/payment_screenshots/'
    )
    
    def __str__(self):
        return f"{self.passenger.full_name}"


class Ride(TimestampedModel):
    driver = models.ForeignKey("driver.Driver", 
                               on_delete=models.CASCADE)

    route = models.ForeignKey("routeline.RouteLine", 
                              on_delete=models.CASCADE, 
                              null=True, 
                              blank=True)

    commission_payment_screenshot = models.ImageField(
        blank=True,
        null=True, 
        upload_to='drivers/comission_payment_screenshots/'
    )

    is_completed = models.BooleanField(default=False)

    bookings = models.ManyToManyField(Booking,
                                      blank=True)

    def __str__(self):
        return f"{self.driver.full_name} - {self.route.name}"


