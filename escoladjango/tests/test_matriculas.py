from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escoladjango.models import Matricula, Estudante, Curso
from escoladjango.serializers import MatriculaSerializer

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
    
    def test_request_get_lista_matricula(self):
        """Testa a requisição GET uma matricula."""
        response = self.client.get(self.url+"1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_srlz = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_srlz)
    
    def test_request_post_criar_matricula(self):
        """Testa a requisição POST de criação de uma matricula."""
        dados = {
            "estudante": self.estudante_1.id,
            "curso": self.curso_1.id,
            "periodo": "V"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_request_delete_matricula(self):
        """Testa a requisição DELETE de deletar uma matricula."""
        response = self.client.delete(f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_request_put_atualizar_matricula(self):
        """Testa a requisição PUT de atualizar uma matricula."""
        dados = {
            "estudante": self.estudante_1.id,
            "curso": self.curso_1.id,
            "periodo": "M"
        }
        response = self.client.put(f"{self.url}1/", dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)