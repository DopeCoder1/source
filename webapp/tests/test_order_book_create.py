from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse
import json


class OrderBookCreateTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/publisher.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/books.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/requests.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/order_books.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/orders.json', verbosity=0)


        self.client = Client()
        self.client.login(login='admin', password="admin")

    def test_details(self):
        response = self.client.get(reverse('webapp:request_book_create', kwargs={'pk': 1}),
                                   {'id': 4, 'request': 1, 'amount': 3})
        self.assertEqual(response.status_code, 200)

