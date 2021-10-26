""" urls for the restaurant app """
from django.urls import path
from . import views

urlpatterns = [
    path('make_booking', views.make_booking, name='make_booking'),
    path(
        'booking_confirmed/<booking_id>',
        views.booking_confirmed, name='booking_confirmed'),
    path('manage_bookings', views.manage_bookings, name='manage_bookings'),
]
