from django.contrib import admin
from .models import TimestampedModel, BaseUserModel


admin.site.register(TimestampedModel)
admin.site.register(BaseUserModel)