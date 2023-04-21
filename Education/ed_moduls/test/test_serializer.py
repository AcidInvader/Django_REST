from django.test import TestCase
from ed_moduls.serializer import EducationModulSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.routers import DefaultRouter

class EducationModulSerializerTest(APITestCase):
    def test_create_modul(self):
        router = DefaultRouter
        url = router('modul')
        data = {"name": "python", "description": "django"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)