from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {
        "estudiantes":[
            {"nombre": "Pablo", "apellido": "Zambrano"},
            {"nombre": "Emanuel", "apellido": "Dautel"},
            {"nombre": "Carlos", "apellido": "Perez"},
            {"nombre": "Manuela", "apellido": "Gomez"}
        ]
        }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_estudiantes.html',
        context = contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos":[
            {"nombre": "Python", "comision": "40440"},
            {"nombre": "Frontend", "comision": "1000"},
            {"nombre": "Python", "comision": "1001"}
        ]
    }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_cursos.html',
        context = contexto,
    )
    return http_response

# Create your views here.
