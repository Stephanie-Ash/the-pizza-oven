""" Admin set-up for the restaurant app"""
from django.contrib import admin
from .models import Restaurant, Table


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """ Admin options for the Restaurant model """
    list_display = ('name', 'opening_time', 'closing_time')
    search_fields = ('name',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Admin options for the Table model """
    list_display = ('restaurant', 'size')
    ordering = ('size',)
