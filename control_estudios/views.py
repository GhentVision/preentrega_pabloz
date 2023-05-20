from django.shortcuts import render, redirect
from django.urls import reverse

from control_estudios.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from control_estudios.models import Estudiante, Curso, Profesor

def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
        }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_estudiantes.html',
        context = contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
        }

    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_cursos.html',
        context = contexto,
    )
    return http_response

def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all(),
        }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_profesores.html',
        context = contexto,
    )
    return http_response

def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(nombre=nombre, comision=comision) 
            curso.save()
            
            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )
    return http_response 

def añadir_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            fecha_nac = data["fecha_nac"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            estudiante = Estudiante(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, dni=dni,email=email,telefono=telefono) 
            estudiante.save()
            
            url_exitosa = reverse('lista_estudiantes')
            return redirect(url_exitosa)
    
    else:
        formulario = EstudianteFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_estudiantes.html',
        context={'formulario': formulario}
    )
    return http_response 
    

def añadir_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            fecha_nac = data["fecha_nac"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            profesion = data["profesion"]
            bio = data["bio"]
            estudiante = Profesor(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, dni=dni,email=email,telefono=telefono,profesion=profesion,bio=bio) 
            estudiante.save()
            
            url_exitosa = reverse('lista_profesores')
            return redirect(url_exitosa)
    else:
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_profesores.html',
        context={'formulario': formulario}
    )
    return http_response 

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__exact=busqueda)
        contexto = {
            "cursos":cursos,
        }

        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto
        )
        return http_response 
    
def buscar_estudiante(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        estudiantes = Estudiante.objects.filter(apellido__icontains=busqueda)
        contexto = {
            "estudiantes":estudiantes,
        }

        http_response = render(
            request=request,
            template_name='control_estudios/lista_estudiantes.html',
            context=contexto
        )
        return http_response 
    
def buscar_profesor(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        profesores = Profesor.objects.filter(apellido__icontains=busqueda)
        contexto = {
            "profesores":profesores,
        }

        http_response = render(
            request=request,
            template_name='control_estudios/lista_profesores.html',
            context=contexto
        )
        return http_response 
        

# Create your views here.
