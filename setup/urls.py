from django.contrib import admin
from django.urls import path, include
from escoladjango.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet,  ListaMatriculaEstudantes, ListaMatriculaCurso
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação API",
      default_version='v1',
      description="Documentação API escolaDjango",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudantes.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
