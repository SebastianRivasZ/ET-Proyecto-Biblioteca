from django.db import models

# Create your models here.

class Libro(models.Model):
    codigo = models.TextField()
    titulo = models.CharField(max_length=50)
    publicacion = models.DateField()
    descripcion = models.TextField()
    imagen = models.TextField()

class Autor(models.Model):
    nombre = models.CharField(max_length=70)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField()
    information = models.TextField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class NavItem(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.CharField(max_length=100)