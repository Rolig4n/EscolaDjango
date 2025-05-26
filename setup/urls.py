from django.contrib import admin
from django.urls import path
from escoladjango.views import estudantes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("estudantes/", estudantes),
]
