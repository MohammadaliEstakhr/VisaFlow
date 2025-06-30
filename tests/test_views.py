from django.test import TestCase
from django.urls import reverse
from core.models import VisaApplication

class VisaApplicationTests(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_submit_view(self):
        response = self.client.get(reverse('submit'))
        self.assertEqual(response.status_code, 200)

    def test_export_pdf_view(self):
        response = self.client.get(reverse('export_pdf'))
        self.assertEqual(response.status_code, 200)
