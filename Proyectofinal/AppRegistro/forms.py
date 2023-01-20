from django import forms
from django.contrib.auth.models import User


class PersonaForm (forms.Form):
    nombre = forms.CharField(label="nombre" )
    apellido = forms.CharField(label="apellido" )
    email = forms.EmailField(label="email" )
    dni = forms.IntegerField(label="dni" )




