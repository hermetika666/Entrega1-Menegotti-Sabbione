from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MiFormularioCreacion(UserCreationForm):

    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña' , widget=forms.PasswordInput)


class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {key:"" for key in fields}


class EditarPerfilFormulario(forms.Form):
    email = forms.CharField(label='E-Mail')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)


class CambiaPasswrd(PasswordChangeForm):
    old_password = forms.CharField(label='Ingrese Contraseña Actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Ingrese Contraseña Nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña Nueva', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']
    help_texts = {key:"" for key in fields}