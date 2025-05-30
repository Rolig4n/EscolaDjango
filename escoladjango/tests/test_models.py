from django.test import TestCase
from escoladjango.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def test_falha(self): teste de falha
    #     self.fail("Teste falhou")
    def setUp(self) -> None:
        self.estudante = Estudante.objects.create(
            nome = "João da Silva",
            email = "joao@joao.com",
            cpf = "77862672046",
            data_nascimento = "2023-02-03",
            numero_celular = "55 44553-4712"
        )
    
    def test_verifica_atrb_estudante(self):
        """"Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, "João da Silva")
        self.assertEqual(self.estudante.email, "joao@joao.com")
        self.assertEqual(self.estudante.cpf, "77862672046")
        self.assertEqual(self.estudante.data_nascimento, "2023-02-03")
        self.assertEqual(self.estudante.numero_celular, "55 44553-4712")

class ModelCursoTestCase(TestCase):
    def setUp(self) -> None:
        self.curso = Curso.objects.create(
            codigo = "DJ1",
            descricao = "Curso de Django",
            nivel = "I"
        )
    
    def test_verifica_atrb_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, "DJ1")
        self.assertEqual(self.curso.descricao, "Curso de Django")
        self.assertEqual(self.curso.nivel, "I")

class ModelMatriculaTestCase(TestCase):
    def setUp(self) -> None:
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            numero_celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',
            descricao='Curso Teste Modelo Matricula',
            nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante_matricula,
            curso = self.curso_matricula,
            periodo = "M"
        )
    
    def test_verifica_atrb_matricula(self):
        """Teste que verifica os atributos do modelo de Matrícula"""
        self.assertEqual(self.matricula.periodo, "M")
        self.assertEqual(self.matricula.estudante.nome, "Teste Modelo Matricula")
        self.assertEqual(self.matricula.curso.descricao, "Curso Teste Modelo Matricula")