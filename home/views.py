# from django.http import HttpResponse
from datetime import datetime
# from django.template import Context, Template, loader
from django.shortcuts import render, redirect
# import random
from home.models import Libreria
from home.forms import LibreriaFormulario, BusquedaLibreriaFormulario
# Clases basadas en listas
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



def nueva_venta(request):

    if request.method == 'POST':
        formulario = LibreriaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
# Atencion: El formato correcto de ingreso es primero el mes y despues el dia
            titulo = data['titulo']
            genero = data['genero']
            mes_venta = data['mes_venta'] or datetime.now()
                
            libro = Libreria(titulo=titulo, genero=genero, mes_venta=mes_venta)
            libro.save()

        return redirect('resumen_ventas')

    formulario = LibreriaFormulario()

    return render(request, 'home/nueva_venta.html', {'formulario': formulario})

#Seteamos el buscador
def resumen_ventas(request):
    titulo = request.GET.get('titulo', None)
    
    if titulo:
        libros = Libreria.objects.filter(titulo__icontains=titulo)
    else:
        libros =Libreria.objects.all()

    formulario = BusquedaLibreriaFormulario()
 
    return render(request, 'home/resumen_ventas.html', {'libros': libros, 'formulario': formulario})

# Para linkear el template que esta en la carpeta STATIC dentro de la app HOME 
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def editar_venta(request, id):
    libro = Libreria.objects.get(id=id)

    if request.method == 'POST':
        formulario = LibreriaFormulario(request.POST)
      
        if formulario.is_valid():
            data = formulario.cleaned_data

            libro.titulo = data['titulo']
            libro.genero = data['genero']
            libro.mes_venta = data['mes_venta'] or datetime.now()
            libro.save()

        return redirect('resumen_ventas')

    formulario = LibreriaFormulario(
        initial={
            'titulo': libro.titulo,
            'genero': libro.genero,
            'mes_venta': libro.mes_venta
        }
    ) 

    return render(request, 'home/editar_venta.html', {'formulario': formulario, 'libro': libro})

def eliminar_venta(request, id):
    libro = Libreria.objects.get(id=id)
    libro.delete()
    return redirect('resumen_ventas')

# ========================
# CLASES BASADAS EN VISTAS
# ========================

class ResumenVentas(ListView):
    model = Libreria
    template_name = 'home/resumen_ventas_cbv.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaLibreriaFormulario()
        return context

class NuevaVenta(CreateView):
    model = Libreria
    success_url = '/resumen-ventas/'
    template_name = 'home/nueva_venta_cbv.html'
    fields =['titulo', 'genero', 'mes_venta', 'descripcion']


class EditarVenta(LoginRequiredMixin, UpdateView):
    model = Libreria
    success_url = '/resumen-ventas/'
    template_name = 'home/editar_venta_cbv.html'
    fields =['titulo', 'genero', 'mes_venta', 'descripcion']


class EliminarVenta(LoginRequiredMixin, DeleteView):
    model = Libreria
    success_url = '/resumen-ventas/'
    template_name = 'home/eliminar_venta_cbv.html'


class VerVenta(DetailView):
    model = Libreria
    template_name = 'home/ver_venta_cbv.html'
 