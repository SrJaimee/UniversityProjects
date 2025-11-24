from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Creacion de una funcion para imprimir una bienvenida, imprime un texto html
def inicio(request):
    return HttpResponse("<h1>Bienvenido a la Pasteleria</h1>")

#Creacion de una funcion para mostrar el documento html
def index(request):
    return render(request, 'paginas/index.html')