#Creacion de una URL para la vista, para preguntarle al usuario que solicitud esta haciendo el usuario
#Para cambiar entre vistas
from django.urls import path
from . import views

#El usuario padra entras y acceder a la vista
#Estructura basica de redireccionamiento
urlpatterns = [
    path('', views.inicio, name='inicio'),
]