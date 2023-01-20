from django.db import models

from django.contrib.auth.models import User 

# Create your models here.


class Persona (models.Model):
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    email= models.EmailField (max_length=50)
    dni= models.IntegerField ()

    def __str__(self):
        return f"{(self.nombre)} - {(self.apellido)} - {(self.email)} - {str(self.dni)}"



