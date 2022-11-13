from django.urls import path
from home import views

# Los que tienen "name" linkea los templates creados como un hipervinculo

urlpatterns = [
    # path('home/', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('resumen-ventas/', views.resumen_ventas, name='resumen_ventas'),
    # path('nueva-venta/', views.nueva_venta, name="nueva_venta"),
    # path('editar-venta/<int:id>', views.editar_venta, name="editar_venta"),
    # path('eliminar-venta/<int:id>', views.eliminar_venta, name="eliminar_venta"),

# Version clases basadas en vistas
       
        path('', views.index, name='index'),
        # path('home/', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('resumen-ventas/', views.ResumenVentas.as_view(), name='resumen_ventas'),
        path('nueva-venta/', views.NuevaVenta.as_view(), name="nueva_venta"),
        path('editar-venta/<int:pk>', views.EditarVenta.as_view(), name="editar_venta"),
        path('eliminar-venta/<int:pk>', views.EliminarVenta.as_view(), name="eliminar_venta"),
        path('ver-venta/<int:pk>', views.VerVenta.as_view(), name="ver_venta"),
] 