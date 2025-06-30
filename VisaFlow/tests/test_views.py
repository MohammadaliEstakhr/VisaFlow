"""
This file contains unit tests for the VisaFlow application views.
It ensures that key pages (home, submit, export) return a successful HTTP response.
"""

from django.test import TestCase
from django.urls import reverse
from core.models import VisaApplication

class VisaApplicationTests(TestCase):
    def test_home_status_code(self):
        """Test that the home page returns status code 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_submit_view(self):
        """Test that the submit page returns status code 200"""
        response = self.client.get(reverse('submit'))
        self.assertEqual(response.status_code, 200)

    def test_export_pdf_view(self):
        """Test that the PDF export page returns status code 200"""
        response = self.client.get(reverse('export_pdf'))
        self.assertEqual(response.status_code, 200)
