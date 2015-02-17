from django.shortcuts import render
from django.http import HttpResponse
#from librokyudo.models import Persona #

# Create your views here.
#este es el controlador realmente, aqui es donde vamos a hacer toda la logistica.
# aqui se usan metodos son "acciones" que igualmente se pueden usar con las classes en el modulo
#metodos se escriben todo en minuscula y con underscore 
#todas las vistas (htmls) deben ponerse en una carpeta que vas a crear manualmente llamada "templates"

#def home(request):
   # return render(request,"index.html")
#def login(request):
    # crear una variable cliente = Persona(esto es el modelo que creaste 
   # cliente = Persona.objects.filter(id=1).first()
    #return render(request,"login.html",{"persona":cliente})
#al hacer esto necesitas igual conectar esto con la url (direccion) para que te ejecute esta acciòn , te tienes que ir a url.py del server
#def saludos(request,personaid):
   # cliente = Persona.objects.filter(id=personaid).first()
    #return render(request,"login.html", {"persona":cliente})

#expresiones regulares leer
#como usar html , template con django

def home_page(request):
    return render(request,'index.html')
