from escoladjango.models import Estudante, Curso, Matricula
from escoladjango.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend as dFilter

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite visualizar ou editar estudantes.
    """
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [dFilter, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite visualizar ou editar cursos.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite visualizar ou editar matrículas.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudantes(generics.ListAPIView):
    """
    Endpoint da API que lista as matrículas de um estudante específico.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Endpoint da API que lista as matrículas de um curso específico.
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer