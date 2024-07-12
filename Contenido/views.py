from django.shortcuts import render
from .models import *

# Create your views here.

def vistaInicio(request):
    context = {
        "Navbar": NavItem.objects.all()
    }
    return render(request, 'content/inicio.html', context)

def vistaLibros(request):
    context = {
        "Libros": Libro.objects.all()
    }
    return render(request, 'content/libros.html', context)

def vistaAutores(request):
    context = {}
    return render(request, 'content/autores.html')

def vistaCategorias(request):
    context = {}
    return render(request, 'content/categorias.html')