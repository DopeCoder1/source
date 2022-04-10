from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse
import json


class PublisherCreateTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/publisher.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/books.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/requests.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/order_books.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/orders.json', verbosity=0)


        self.client = Client()
        self.client.login(login='admin', password="admin")

    def test_details(self):
        response = self.client.post(reverse('webapp:publisher_delete', kwargs={'pk': 5}))
        self.assertEqual(response.status_code, 302)