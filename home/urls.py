from django.urls import path
from home import views

# Los que tienen "name" linkea los templates creados como un hipervinculo

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ver-ventas/', views.ver_ventas, name='ver_ventas'),
    path('nuevas-ventas/', views.home_libreria, name="home_libreria"),
]  