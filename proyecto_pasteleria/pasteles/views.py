from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Creacion de una funcion para imprimir una bienvenida
def inicio(request):
    return HttpResponse("<h1>Bienvenido a la Pasteleria</h1>")