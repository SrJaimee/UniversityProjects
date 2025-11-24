from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Creacion de una funcion para imprimir una bienvenida, imprime un texto html
def inicio(request):
    return render(request, 'paginas/inicio.html')

#Creacion de una funcion para mostrar el documento html
def index(request):
    return render(request, 'paginas/inventario.html')

#Creacion de una funcion para mostar el documento registro (Que es el index de registro)
def gestionarDatos(request):
    return render(request, 'gestionarDatos/registros.html')