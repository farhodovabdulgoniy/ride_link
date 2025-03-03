from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    DriverListAPIView,
    DriverDetailAPIView,
    PassengerListAPIView,
    PassengerDetailAPIView,

    RideViewSet,
    BookingViewSet,
    CarModelViewSet, 
    RouteLineViewSet,
    TariffViewSet,
    DriverTariffViewSet,
)


router = DefaultRouter()
router.register(r'routelines', RouteLineViewSet, basename='dashboard-routelines')
router.register(r'rides', RideViewSet, basename='dashboard-rides')
router.register(r'bookings', BookingViewSet, basename='dashboard-bookings')
router.register(r'carmodels', CarModelViewSet, basename='dashboard-carmodels')
router.register(r'tariffs', TariffViewSet, basename='dashboard-tariffs')
router.register(r'drivertariffs', DriverTariffViewSet, basename='dashboard-drivertariffs')


urlpatterns = [
    path('', include(router.urls)),

    path('drivers/', DriverListAPIView.as_view()),
    path('drivers/<int:pk>/', DriverDetailAPIView.as_view()),

    path('passengers/', PassengerListAPIView.as_view()),
    path('passengers/<int:pk>/', PassengerDetailAPIView.as_view()),
]
