from django.shortcuts import render
from .models import *

# Create your views here.

def vistaInicio(request):
    context = {
        "NavItem": NavItem.objects.all()
    }
    return render(request, 'content/inicio.html', context)

def vistaLibros(request):
    context = {
        "NavItem": NavItem.objects.all(),
        "Libros": Libro.objects.all()
    }
    return render(request, 'content/libros.html', context)

def vistaAutores(request):
    context = {
        "NavItem": NavItem.objects.all(),
        "Autores": Autor.objects.all()
    }
    return render(request, 'content/autores.html', context)

def vistaCategorias(request):
    context = {
        "NavItem": NavItem.objects.all(),
        "Categorias": Categoria.objects.all()
    }
    return render(request, 'content/categorias.html', context)