from django.db import models

from base.models import BaseUserModel


class Passenger(BaseUserModel):
    promo_code = models.CharField(max_length=15, 
                                  blank=True, 
                                  null=True)

    cashback_percentage = models.PositiveIntegerField(default=0,
                                                      help_text='in percentage %')