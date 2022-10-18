from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import LibreriaFormulario, BusquedaLibreriaFormulario 

from home.models import Libreria

def home_libreria(request):

    if request.method == 'POST':

        formulario = LibreriaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            titulo = data['titulo']
            genero = data['genero']
            mes_venta = data['mes_venta']
            
            libro = Libreria(titulo=titulo, genero=genero, mes_venta=mes_venta)
            libro.save()

        return redirect('ver_ventas')

    formulario = LibreriaFormulario()

    return render(request, 'home/home_libreria.html', {'formulario': formulario})

#Seteamos el buscador
def ver_ventas(request):
    titulo = request.GET.get('titulo', None)
    
    if titulo:
        libros = Libreria.objects.filter(titulo__icontains=titulo)
    else:
        libros =Libreria.objects.all()

    formulario = BusquedaLibreriaFormulario()
 
    return render(request, 'home/ver_ventas.html', {'libros': libros, 'formulario': formulario})

# Para linkear el template que esta en la carpeta STATIC dentro de la app HOME 
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html') 