"""
URL configuration for proyecto_preentrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes, listar_cursos, listar_profesores, crear_curso, añadir_estudiante, añadir_profesor,buscar_cursos, buscar_estudiante, buscar_profesor

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("nuevo-estudiante/", añadir_estudiante, name="nuevo_estudiante"),
    path("buscar-estudiante/", buscar_estudiante, name="buscar_estudiante"),
    path("profesores/", listar_profesores, name="lista_profesores"),
    path("nuevo-profesor/", añadir_profesor, name="nuevo_profesor"),
    path("buscar-profesor/", buscar_profesor, name="buscar_profesor"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
]


