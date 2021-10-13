""" Views for the restaurant app """
from django.shortcuts import render
from .models import Restaurant


def index(request):
    """
    A view to return the homepage with restaurant information populated
    """
    restaurant = Restaurant.objects.get(name="The Pizza Oven")
    context = {
        'restaurant': restaurant,
    }

    return render(request, 'restaurant/index.html', context)
