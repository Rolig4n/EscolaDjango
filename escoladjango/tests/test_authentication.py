from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.url = reverse("Estudantes-list")

    def test_authentication_cred_certas(self):
        """"Testa se o usuário esta com as credenciais corretas."""
        usuario = authenticate(username="admin", password="admin")
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_authentication_cred_username_errada(self):
        """"Testa se o usuário esta com as credenciais incorretas."""
        usuario = authenticate(username="admn", password="admin")
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_authentication_cred__senha_errada(self):
        """"Testa se o usuário esta com as credenciais incorretas."""
        usuario = authenticate(username="admin", password="adm")
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
    
    def test_request_get_autorizada(self):
        """Testa se a requisição /Estudantes GET é autorizada."""
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_não_autorizada(self):
        """Testa se a requisição /Estudantes GET é autorizada."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
