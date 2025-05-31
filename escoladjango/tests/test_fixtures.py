from django.test import TestCase
from escoladjango.models import Estudante, Curso, Matricula

class FixturesTestCase(TestCase):
    fixtures = ["proto_banco.json"]

    def test_load_fixtures(self):
        """Testa se os fixtures foram carregados corretamente."""
        estudante = Estudante.objects.get(cpf="03349600883")
        curso = Curso.objects.get(pk=4)
        self.assertEqual(estudante.numero_celular, "68 98765-4622")
        self.assertEqual(curso.codigo, "CDJ01")