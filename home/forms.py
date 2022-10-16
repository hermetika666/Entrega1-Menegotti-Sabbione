from mailbox import NoSuchMailboxError
from django import forms

class HumanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    # requiered=false de arriba sirve para que el campo no sea requerido para que si o si se complete
