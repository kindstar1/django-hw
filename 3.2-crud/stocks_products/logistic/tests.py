"""
Тест API для CI: проверка доступности эндпоинта списка продуктов.
"""
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ProductAPITestCase(TestCase):
    """Проверка GET /api/v1/products/."""

    def setUp(self):
        self.client = APIClient()

    def test_products_list_returns_200(self):
        """Список продуктов возвращает 200."""
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
