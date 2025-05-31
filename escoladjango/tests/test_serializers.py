from django.test import TestCase
from escoladjango.models import Estudante, Curso, Matricula
from escoladjango.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class EstudanteSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "João da Silva",
            email = "joao@joao.com",
            cpf = "77862672046",
            data_nascimento = "2023-02-03",
            numero_celular = "55 44553-4712"
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)
    
    def test_verifica_campos_serializer_estudante(self):
        """Teste que verifica os campos do serializer de Estudante"""
        data = self.serializer_estudante.data
        self.assertEqual(set(data.keys()), set(["nome", "id", "email", "cpf", "data_nascimento", "numero_celular"]))
        
    def test_verifica_conteudo_serializer_estudante(self):
        """Teste que verifica o conteudo dos campos do serializer de Estudante"""
        data = self.serializer_estudante.data
        self.assertEqual(data["nome"], self.estudante.nome)
        self.assertEqual(data["email"], self.estudante.email)
        self.assertEqual(data["cpf"], self.estudante.cpf)
        self.assertEqual(data["data_nascimento"], self.estudante.data_nascimento)
        self.assertEqual(data["numero_celular"], self.estudante.numero_celular)
    
class CursoSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "DJ1",
            descricao = "Curso de Django",
            nivel = "I"
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)
    
    def test_verifica_campos_serializer_curso(self):
        """Teste que verifica os campos do serializer de Curso"""
        data = self.serializer_curso.data
        self.assertEqual(set(data.keys()), set(["codigo", "id", "descricao", "nivel"]))
        
    def test_verifica_conteudo_serializer_curso(self):
        """Teste que verifica o conteudo dos campos do serializer de Curso"""
        data = self.serializer_curso.data
        self.assertEqual(data["codigo"], self.curso.codigo)
        self.assertEqual(data["descricao"], self.curso.descricao)
        self.assertEqual(data["nivel"], self.curso.nivel)

class MatriculaSerializerTestCase(TestCase):
    def setUp(self):
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
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
    
    def test_verifica_campos_serializer_matricula(self):
        """Teste que verifica os campos do serializer de Matrícula"""
        data = self.serializer_matricula.data
        self.assertEqual(set(data.keys()), set(["id", "periodo", "estudante", "curso"]))
    
    def test_verifica_conteudo_serializer_matricula(self):
        """Teste que verifica o conteudo dos campos do serializer de Matrícula"""
        data = self.serializer_matricula.data
        self.assertEqual(data["periodo"], self.matricula.periodo)
        self.assertEqual(data["estudante"], self.matricula.estudante.id)
        self.assertEqual(data["curso"], self.matricula.curso.id)