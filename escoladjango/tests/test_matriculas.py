from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escoladjango.models import Matricula, Estudante, Curso
from escoladjango.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    fixtures = ["proto_banco.json"]

    def setUp(self):
        # self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.usuario = User.objects.get(username="admin")
        self.url = reverse("Matriculas-list")
        self.client.force_authenticate(user=self.usuario)

        self.estudante_1 = Estudante.objects.get(pk=1)
        self.curso_1 = Curso.objects.get(pk=1)
        self.matricula_1 = Matricula.objects.get(pk=1)
    
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