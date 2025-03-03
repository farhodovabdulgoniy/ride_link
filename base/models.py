from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BaseUserModel(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    telegram_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.full_name