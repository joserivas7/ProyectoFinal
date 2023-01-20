from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio, name="inicio"),
    path('register/',register, name="register"),
    path('login/', login_register, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),


    path('crearblog/', crearblog, name="crearblog"),
    path('crearmensaje/', crearmensaje, name="crearmensaje"),


    path('about/',about, name="about"),
    path('pagina2/',pagina2, name="pagina2"),

    
    path('blog/<id>',blog, name="blog"),
    path('blog1/',blog1, name="blog1"),
    path('blog2/',blog2, name="blog2"),
    path('blog3/',blog3, name="blog3"),
    path('blog4/',blog4, name="blog4"),
    path('blog5/',blog5, name="blog5"),

    path('construccion/',construccion, name="construccion"),


    path('buscar/',buscar, name="buscar"),
    path('busquedatitulo/', busquedatitulo, name="busquedatitulo"),

    
    path('eliminarblog/<id>',eliminarblog, name="eliminarblog"),
    path('editarblog/<id>',editarblog, name="editarblog"),
    path('editarperfil/', editarperfil, name="editarperfil"),
    path('editaravatar/', editaravatar, name="editaravatar"),


    path('listadeblog/', listadeblog, name="listadeblog"),
    path('listademensaje/', listademensaje, name="listademensaje"),

]


