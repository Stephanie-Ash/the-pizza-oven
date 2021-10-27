""" urls for the restaurant app """
from django.urls import path
from . import views

urlpatterns = [
    path('make_booking', views.make_booking, name='make_booking'),
    path(
        'booking_confirmed/<booking_id>',
        views.booking_confirmed, name='booking_confirmed'),
    path('manage_bookings', views.manage_bookings, name='manage_bookings'),
    path('add_table_no/<booking_id>', views.add_table_no, name='add_table_no'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_booking'),
]
