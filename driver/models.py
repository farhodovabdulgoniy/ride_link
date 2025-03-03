from django.db import models

from base.models import BaseUserModel

from tariff.models import DriverTariff


class CarModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    car_type = models.CharField(max_length=20, 
        choices=[
            ('Start', 'Start'), 
            ('Comfort', 'Comfort'), 
            ('Lux', 'Lux')
        ]
    )
    
    def __str__(self):
        return f"{self.name} ({self.car_type})"


class Driver(BaseUserModel):
    car_number = models.CharField(max_length=8, unique=True)
    car_model = models.ForeignKey(CarModel, 
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
                                  
    is_paid_comission = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)

    tariff = models.ForeignKey("tariff.Tariff",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)

    def has_active_tariff(self):
        return DriverTariff.objects.filter(driver=self, is_paid=True).exists()


    def __str__(self):
        return f"{self.full_name} | {self.car_number} | {self.car_model.name}"