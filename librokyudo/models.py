from django.db import models

# Create your models here.
#class es representacion de un objeto real que tiene atributos
class Flecha(models.Model):
    acierto = models.BooleanField(default = None)
    fecha = models.DateTimeField()
    ronda = models.ForeignKey("Ronda")

class Ronda(models.Model):
    fecha = models.DateTimeField() #usar Foreignkey para relacionar este atributo a un modelo (conjunto) 
    tirador = models.ForeignKey("Persona")

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    clave = models.CharField(max_length=10)
    #imagen = 
    def __str__(self):
        return self.nombre
    #al cambiar o hacer cualquier cambio en models.py llamar comando: manage.py makemigrations 
    #Opcional puedes llamar: manage.py migrate    