from django.shortcuts import render
from home.models import Libreria
from home.forms import BusquedaLibreriaFormulario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
     return render(request, 'home/index.html')

def about(request):
     return render(request, 'home/about.html')


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
    
