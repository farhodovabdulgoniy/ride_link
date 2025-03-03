from django.contrib import admin
from .models import Tariff, DriverTariff


admin.site.register(Tariff)
admin.site.register(DriverTariff)