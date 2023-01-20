from django.shortcuts import render
from django.http import HttpResponse

from AppFinal.forms import BlogsForm, RegisterUsuarioForm, EditarUsuarioForm , AvatarForm , UserCreationForm , MensajeForm
from AppFinal.models import Blogs , Avatar , Mensaje



from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 



def inicio(request):
    return render(request, "AppFinal/Inicio.html" ,{ "avatar": obtenerAvatar(request)})

def about(request):
    return render(request, "AppFinal/about.html" ,{ "avatar": obtenerAvatar(request)})

def pagina2(request):
    return render(request, "AppFinal/pagina2.html" ,{ "avatar": obtenerAvatar(request)})

def construccion(request):
    return render(request, "AppFinal/construccion.html" ,{ "avatar": obtenerAvatar(request)})



#Blogs inicios

def blog1(request):
    return render(request, "AppFinal/blog1.html", { "avatar": obtenerAvatar(request)})

def blog2(request):
    return render(request, "AppFinal/blog2.html" , { "avatar": obtenerAvatar(request)})

def blog3(request):
    return render(request, "AppFinal/blog3.html", { "avatar": obtenerAvatar(request)})

def blog4(request):
    return render(request, "AppFinal/blog4.html", { "avatar": obtenerAvatar(request)})

def blog5(request):
    return render(request, "AppFinal/blog5.html", { "avatar": obtenerAvatar(request)})




#Muestra el avatar en todas las Views

def obtenerAvatar(request):
        lista=Avatar.objects.filter(user=request.user.id)
        if len(lista)!=0:
            avatar=lista[0].imagen.url
        else:
            avatar="/media/avatars/defaul.png"
        return avatar



#Todo sobre usuarios

def register(request):
    if request.method=="POST":
        form= RegisterUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppFinal/register.html", {"mensaje": f"usuario {username} creado correctamente"} )
        else:
            return render(request, "AppFinal/register.html", {"form": form, "mensaje":"Error al crear el usuario."})
    else:
        form= RegisterUsuarioForm()
        return render (request, "AppFinal/register.html", {"form": form})
        
    
def login_register(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppFinal/inicio.html", {"mensaje": f"{usu} logeado correctamente.", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "AppFinal/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta."})
        else:        
            return render(request, "AppFinal/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta."})
    else:
        form= AuthenticationForm()
        return render(request, "AppFinal/login.html", {"form": form})


@login_required
def editarperfil(request):
    usuario= request.user
    if request.method=="POST":
        form=EditarUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppFinal/editarperfil.html" , { "mensaje": f"Usuario {usuario.username} editado correctamente." , "avatar": obtenerAvatar(request)} )
        else:
            return render(request, "AppFinal/editarperfil.html" , {"form" : form , "nombreusuario":usuario.username , "avatar": obtenerAvatar(request)})
    else:
        form=EditarUsuarioForm(instance=usuario)
        return render(request, "AppFinal/editarperfil.html" , {"form" : form , "nombreusuario":usuario.username , "avatar": obtenerAvatar(request)} )


@login_required
def editaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
            avatar.save()
            return render(request, "AppFinal/editaravatar.html" , {"mensaje": "Avatar agregado correctamente." , "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppFinal/editaravatar.html" , {"form": form, "usuario":request.user, "mensaje": "Error al agregar el Avatar." , "avatar": obtenerAvatar(request) })
    else:
        form=AvatarForm()
        return render(request, "AppFinal/editaravatar.html", {"form": form, "usuario": request.user , "avatar": obtenerAvatar(request)})





#Todo sobre Blogs

def crearblog (request):
    if request.method=="POST":
        form= BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data #convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            parrafo= informacion["parrafo"]
            parrafoamplio= informacion["parrafoamplio"]
            autor= informacion["autor"]
            creado= informacion["creado"]
            imagen= informacion["imagen"]
            blo= Blogs(titulo=titulo, subtitulo=subtitulo, parrafo=parrafo, parrafoamplio=parrafoamplio, autor=autor, imagen=imagen, creado=creado)
            blo.save()
            return render(request, "AppFinal/crearblog.html", {"mensaje": "Blog guardado",  "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppFinal/crearblog.html", {"mensaje2": "Informacion no Valida para guardar." ,  "avatar": obtenerAvatar(request)})
    else:
        formulario= BlogsForm()
        return render(request, "AppFinal/crearblog.html", {"form": formulario ,  "avatar": obtenerAvatar(request)})



def eliminarblog(request, id):
    ti= Blogs.objects.get(id=id)
    ti.delete()
    titu= Blogs.objects.all()
    return render(request, "AppFinal/resultadoautor.html", {"autor": titu, "mensaje": "Blog eliminado." ,  "avatar": obtenerAvatar(request)})


def listadeblog (request):
    blogs= Blogs.objects.filter()
    return render(request, "AppFinal/listadeblog.html", {"blog" : blogs ,"avatar": obtenerAvatar(request)})



def editarblog (request, id):
    edi=Blogs.objects.get(id=id)
    if request.method=="POST":
        form= BlogsForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            edi.titulo=info["titulo"]
            edi.subtitulo=info["subtitulo"]
            edi.parrafo=info["parrafo"]
            edi.parrafoamplio=info["parrafoamplio"]
            edi.autor=info["autor"]
            edi.creado=info["creado"]
            edi.imagen=info["imagen"]
            edi.save()
            blogs=Blogs.objects.all()
            return render(request, "AppFinal/listadeblog.html", { "blogs":blogs ,"mensaje":"Blog editado correctamente." ,  "avatar": obtenerAvatar(request)})
    else:
        formulario= BlogsForm(initial={"titulo":edi.titulo, "subtitulo":edi.subtitulo, "parrafo":edi.parrafo, "parrafoamplio":edi.parrafoamplio, "autor":edi.autor ,"creado":edi.creado , "imagen":edi.imagen,  "avatar": obtenerAvatar(request)})
        return render(request, "AppFinal/editarblog.html", {"form": formulario, "blogs": edi ,  "avatar": obtenerAvatar(request)})


def busquedatitulo (request):
    return render(request, "AppFinal/busquedatitulo.html" ,{ "avatar": obtenerAvatar(request)} )


def buscar (request):
    titulo= request.GET["titulo"]
    if titulo!="":
        titu= Blogs.objects.filter(titulo__icontains=titulo)
        return render(request, "AppFinal/resultadoautor.html" ,{"titu":titu , "avatar": obtenerAvatar(request)})
    else:
        return render(request, "AppFinal/busquedatitulo.html", {"mensaje":"Ingresa por favor un Titulo.", "avatar": obtenerAvatar(request)})



def blog(request, id):
    blogs= Blogs.objects.filter(id=id)
    return render(request, "AppFinal/blog.html", {"blogs" : blogs ,"avatar": obtenerAvatar(request)})





# Chat de mensajeria 

def crearmensaje (request):
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data #convierte el formulario en un diccionario para poder manejarlo y guardarlo en la DB.
            emisor= informacion["emisor"]
            receptor= informacion["receptor"]
            cuerpo= informacion["cuerpo"]
            men= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo)
            men.save()
            return render(request, "AppFinal/crearmensaje.html", {"mensaje": "Mensaje enviado.",  "avatar": obtenerAvatar(request)})
        else:
            return render(request, "AppFinal/crearmensaje.html", {"mensaje2": "Informacion no Valida para enviar." ,  "avatar": obtenerAvatar(request)})
    else:
        formulario= MensajeForm()
        return render(request, "AppFinal/crearmensaje.html", {"form": formulario ,  "avatar": obtenerAvatar(request)})



def listademensaje(request):
    msj= Mensaje.objects.filter()
    return render(request, "AppFinal/listademensaje.html", {"msj" : msj ,"avatar": obtenerAvatar(request)})