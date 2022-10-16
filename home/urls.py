from django.urls import path
from home import views
# from . import views

# Los que tienen name son para linkear los templates creados como un hypervinculo

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('fecha/', views.fecha, name='fecha'),
    # path('mi-template/', views.mi_template, name='mi_template'),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    # path('crear-personas/<str:nombre>/<str:apellido>/', views.home_persona),
    path('crear-persona/', views.home_persona, name="home_persona"),
    
]  