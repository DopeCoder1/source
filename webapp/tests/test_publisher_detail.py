from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class PublisherDetailTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/publisher.json', verbosity=0)

        self.client = Client()
        self.client.login(login='admin', password="admin")

    def test_details(self):
        response = self.client.get(reverse('webapp:publisher_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('publisher' in response.context)


