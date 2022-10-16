from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random

from home.models import Humano

def hola(request):
    return HttpResponse('<h1>Hola Amigos!</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu año de nacimiento aproximado para tu {edad} edad seria: {fecha}')

def mi_template(request):

    cargar_archivo = open(r'C:\Programacion\Django\Proyecto\home\Templates\mi_template.html',  'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def tu_template(request, nombre):

    template = loader.get_template('home/tu_template.html')
    template_renderizado = template.render({'persona': nombre})

    return HttpResponse(template_renderizado)

def prueba_template(request):

    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)        
     }

    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)

# def home_persona(request, nombre, apellido):

    # persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    # persona.save()
def home_persona(request):

    if request.method == 'POST':
    # print('POST')
    # print(request.POST)
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        persona = Humano(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_creacion=datetime.now())
        persona.save()

        return redirect('ver_personas')

    # template = loader.get_template('home/home_persona.html')
    # template_renderizado = template.render({'persona': persona})

    # return HttpResponse(template_renderizado)

    return render(request, 'home/home_persona.html', {})

def ver_personas(request):

    personas = Humano.objects.all()

    # template = loader.get_template('home/ver_personas.html')
    # template_renderizado = template.render({'personas': personas})
    # return HttpResponse(template_renderizado)
 
    return render(request, 'home/ver_personas.html', {'personas': personas})

# Para linkear el template que esta en la carpeta STATIC dentro de la app HOME
def index(request):

    return render(request, 'home/index.html')