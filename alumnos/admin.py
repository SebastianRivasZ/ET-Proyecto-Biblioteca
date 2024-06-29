from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Genero, Alumno, Curso, Navbar

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Navbar)