from django.contrib import admin
from .models import Restaurant, Table


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'opening_time', 'closing_time')
    search_fields = ('name',)


@admin.register(Table)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'size')
    ordering = ('size',)
