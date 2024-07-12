from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.vistaInicio, name="index"),
	path('libros', views.vistaLibros, name="libros"),
	path('autores', views.vistaAutores, name="autores"),
	path('categorias', views.vistaCategorias, name="categorias"),
] 