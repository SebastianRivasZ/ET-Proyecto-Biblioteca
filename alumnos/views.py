from django.shortcuts import render

# Create your views here.
def index(request):
    Alumnos = Alumno.objects.all() # select * from Alumno
    Cursos = Curso.objects.all() # select * from Curso 
    Navbar = Navbar.objects.all() # select * from Navbar
    context = {
        "Alumnos": Alumnos,
        "Cursos": Cursos,
        "Navbar": Navbar
    }
    return render(request, 'alumnos/index.html', context)

def misAsignaturas(request):
    context = {}
    return render(request, 'alumnos/misAsignaturas.html', context)