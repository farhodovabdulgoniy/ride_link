from django.db import models

from base.models import TimestampedModel

from datetime import timedelta


class Tariff(TimestampedModel):
    name = models.CharField(max_length=255, unique=True)

    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)

    duration_days = models.PositiveIntegerField(default=30)

    ride_limit = models.PositiveIntegerField(default=10)

    comission = models.PositiveIntegerField(default=5,
                                            help_text="in percentage %")
    
    def __str__(self):
        return self.name


class DriverTariff(TimestampedModel):
    driver = models.ForeignKey("driver.Driver", 
                               on_delete=models.CASCADE)

    selected_tariff = models.ForeignKey(Tariff, 
                               on_delete=models.CASCADE)

    is_paid = models.BooleanField(default=False)

    tariff_payment_screenshot = models.ImageField(
        upload_to='drivers/tariff_payment_screenshots/',
        null=True,
        blank=True
    )

    paid_at = models.DateTimeField(null=True, blank=True)

    tariff_end = models.DateTimeField(null=True, blank=True) 

    class Meta:
        unique_together = ('driver', 'selected_tariff')

    def save(self, *args, **kwargs):
        if self.paid_at and self.selected_tariff:
            self.tariff_end = self.paid_at + timedelta(days=self.selected_tariff.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.driver.full_name} | {self.selected_tariff.name}"