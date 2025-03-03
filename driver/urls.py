from django.urls import path

from .views import RideCreateAPIView


urlpatterns = [
    path('create-ride/', RideCreateAPIView.as_view()),
]