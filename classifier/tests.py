from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class NumberClassifierTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_valid_number(self):
        """Test with valid number input."""
        response = self.client.get(
            reverse('classify-number'),
            {'number': '371'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number'], 371)
        self.assertIn('armstrong', response.data['properties'])
        self.assertIn('odd', response.data['properties'])
        
    def test_invalid_input(self):
        """Test with invalid input."""
        response = self.client.get(
            reverse('classify-number'),
            {'number': 'abc'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data['error'])
        
    def test_missing_parameter(self):
        """Test with missing number parameter."""
        response = self.client.get(reverse('classify-number'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)