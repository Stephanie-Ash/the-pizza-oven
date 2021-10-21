""" urls for the restaurant app """
from django.urls import path
from . import views

urlpatterns = [
    path('make_booking', views.make_booking, name='make_booking'),
]
