from django.db import models
from ckeditor.fields import RichTextField

class Libreria(models.Model):
    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    # mes_venta = models.CharField(max_length=30)
    mes_venta = models.DateField()
    descripcion = RichTextField(null=True)
    
    def __str__(self) -> str:
        return f'Titulo: {self.titulo} - Genero: {self.genero} - Fecha de Venta: {self.mes_venta}'