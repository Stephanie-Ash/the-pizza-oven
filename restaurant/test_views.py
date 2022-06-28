""" Testcases for the restaurant app views. """
from django.test import TestCase

from .models import Restaurant


class TestViews(TestCase):
    """ Tests for the views. """

    def test_get_index_page(self):
        """ Test the index page view. """
        Restaurant.objects.create(name='The Pizza Oven')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant/index.html')
