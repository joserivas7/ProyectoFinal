from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('crearpersona/', crearpersona, name="crearpersona"),
    path('listadepersonas/', listadepersonas, name="listadepersonas"),



]

