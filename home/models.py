from django.db import models

class Humano(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(null=True)
    # Le pusimos null=true para que pueda venir vacio
   
#    Para que se muestren los nombre de las personas bien en la URL y no como ID Objeto

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'