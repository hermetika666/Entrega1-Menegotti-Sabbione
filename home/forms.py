from mailbox import NoSuchMailboxError
from django import forms

class LibreriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    mes_venta = forms.CharField(max_length=30)
    
class BusquedaLibreriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)