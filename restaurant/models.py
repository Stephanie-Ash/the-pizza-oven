""" Models for the restaurant app """
import datetime
from django.db import models
from cloudinary.models import CloudinaryField


class Restaurant(models.Model):
    """ Model to add information about the restuarant """
    name = models.CharField(max_length=50)
    description = models.TextField()
    opening_time = models.TimeField(
        auto_now=False, auto_now_add=False, default=datetime.time(11, 00, 00))
    closing_time = models.TimeField(
        auto_now=False, auto_now_add=False, default=datetime.time(23, 00, 00))
    menu = CloudinaryField('image', default='placeholder', use_filename=True)

    def __str__(self):
        return self.name
