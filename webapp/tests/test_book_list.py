from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from django.conf import settings
from django.urls import reverse


class BookDetailTests(TestCase):
    def setUp(self):
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/publisher.json', verbosity=0)
        call_command('loaddata', settings.BASE_DIR + '/webapp/tests/fixtures/books.json', verbosity=0)

        self.client = Client()
        self.client.login(login='admin', password="admin")

    def test_details(self):
        response = self.client.get(reverse('webapp:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('book_list' in response.context)
        self.assertEqual(len(response.context['book_list']), 6)