from django.urls import path

from .views import (
    DriverQueueAPIView,
    BookingCreateAPIView,
)


urlpatterns = [
    path('active-drivers/', DriverQueueAPIView.as_view()),
    path('create-booking/', BookingCreateAPIView.as_view()),
]