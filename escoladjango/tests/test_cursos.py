from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escoladjango.models import Curso
from escoladjango.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.url = reverse("Cursos-list")
        self.client.force_authenticate(user=self.usuario)

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
    
    def test_request_get_lista_cursos(self):
        """Testa a requisição GET da lista de cursos."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_lista_curso(self):
        """Testa a requisição GET um curso."""
        response = self.client.get(self.url+"1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_srlz = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_srlz)
    
    def test_request_post_criar_curso(self):
        """Testa a requisição POST de criação de um curso."""
        dados = {
            "codigo": "DJ4",
            "descricao": "Curso de Django Avançado",
            "nivel": "A"
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_curso(self):
        """Testa a requisição DELETE de deletar um curso."""
        response = self.client.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_put_atualizar_curso(self):
        """Testa a requisição PUT de atualizar um curso."""
        dados = {
            "codigo": "DJ2",
            "descricao": "Curso de Django Atualizado",
            "nivel": "I"
        }
        response = self.client.put(f"{self.url}1/", dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)