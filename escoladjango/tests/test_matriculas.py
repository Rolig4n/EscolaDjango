from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escoladjango.models import Matricula, Estudante, Curso

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.url = reverse("Matriculas-list")
        self.client.force_authenticate(user=self.usuario)

        self.estudante_1 = Estudante.objects.create(
            nome = "Teste Estudante 1",
            email="testeestudante1@gmail.com",
            cpf="91546870040",
            data_nascimento="2003-02-02",
            numero_celular="86 99999-9989"
        )
        self.estudante_2 = Estudante.objects.create(
            nome = "Teste Estudante 2",
            email="testeestudante2@gmail.com",
            cpf="85020072036",
            data_nascimento="2003-02-02",
            numero_celular="86 99999-9998"
        )
        self.curso_1 = Curso.objects.create(
            codigo = "DJ2",
            descricao = "Curso de Django",
            nivel = "I"
        )
        self.curso_2 = Curso.objects.create(
            codigo = "DJ3",
            descricao = "Curso de Django",
            nivel = "I"
        )
        self.matricula_1 = Matricula.objects.create(
            estudante = self.estudante_1,
            curso = self.curso_2,
            periodo = "V"
        )
        self.matricula_1 = Matricula.objects.create(
            estudante = self.estudante_2,
            curso = self.curso_1,
            periodo = "M"
        )
    
    def test_request_get_lista_matriculas(self):
        """Testa a requisição GET da lista de matriculas."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)