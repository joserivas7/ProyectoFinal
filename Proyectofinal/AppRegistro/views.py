from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

from AppFinal.views import obtenerAvatar

from AppRegistro.models import Persona
from AppRegistro.forms import PersonaForm 




# Registros para contactar a personas que quieran trabajar en nuestro Site

def crearpersona (request):
    if request.method=="POST":
        form= PersonaForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data #convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            dni= informacion["dni"]
            blo= Persona(nombre=nombre, apellido=apellido, email=email, dni=dni)
            blo.save()
            return render(request, "AppRegistro/crearpersona.html", {"mensaje": "Contacto guardado",  "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppRegistro/crearpersona.html", {"mensaje2": "Informacion no Valida para guardar." ,  "avatar": obtenerAvatar(request)})
    else:
        formulario= PersonaForm()
        return render(request, "AppRegistro/crearpersona.html", {"form": formulario ,  "avatar": obtenerAvatar(request)})


@login_required
def listadepersonas (request):
    Perso= Persona.objects.filter()
    return render(request, "AppRegistro/listadepersonas.html", {"Perso" : Perso ,"avatar": obtenerAvatar(request)})



