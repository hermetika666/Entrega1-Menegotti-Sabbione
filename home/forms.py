from mailbox import NoSuchMailboxError
from django import forms
from ckeditor.fields import RichTextFormField

class LibreriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    mes_venta = forms.DateField()
    

class Libreria(forms.Form):
    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    mes_venta = forms.DateField()
    descripcion = RichTextFormField(required=False)


class BusquedaLibreriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)