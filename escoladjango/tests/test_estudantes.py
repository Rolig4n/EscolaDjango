from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escoladjango.models import Estudante
from escoladjango.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ["proto_banco.json"]

    def setUp(self):
        # self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.usuario = User.objects.get(username="admin")
        self.url = reverse("Estudantes-list")
        self.client.force_authenticate(user=self.usuario)

        # self.estudante_1 = Estudante.objects.create(
        #     nome = "Teste Estudante 1",
        #     email="testeestudante1@gmail.com",
        #     cpf="91546870040",
        #     data_nascimento="2003-02-02",
        #     numero_celular="86 99999-9989"
        # )
        self.estudante_1 = Estudante.objects.get(pk=1)
        # self.estudante_2 = Estudante.objects.create(
        #     nome = "Teste Estudante 2",
        #     email="testeestudante2@gmail.com",
        #     cpf="85020072036",
        #     data_nascimento="2003-02-02",
        #     numero_celular="86 99999-9998"
        # )
        self.estudante_2 = Estudante.objects.get(pk=2)
    
    def test_request_get_lista_estudantes(self):
        """Testa a requisição GET da lista de estudantes."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_lista_estudante(self):
        """Testa a requisição GET um estudante."""
        response = self.client.get(self.url+"1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_srlz = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_srlz)

    def test_request_post_criar_estudante(self):
        """Testa a requisição POST de criação de um estudante."""
        dados = {
            "nome": "teste",
            "email": "testepost@teste.com",
            "cpf": "85429771066",
            "data_nascimento": "2000-01-01",
            "numero_celular": "11 91234-5678"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_request_delete_estudante(self):
        """Testa a requisição DELETE de deletar um estudante."""
        response = self.client.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_put_atualizar_estudante(self):
        """Testa a requisição PUT de atualizar um estudante."""
        dados = {
            "nome": "teste",
            "email": "testeput@teste.com",
            "cpf": "94511442002",
            "data_nascimento": "2000-01-01",
            "numero_celular": "11 91234-5678"
        }
        response = self.client.put(f"{self.url}1/", data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
