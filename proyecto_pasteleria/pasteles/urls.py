#Creacion de una URL para la vista, para preguntarle al usuario que solicitud esta haciendo el usuario
#Para cambiar entre vistas
from django.urls import path
from . import views

#El usuario padra entras y acceder a la vista
#Estructura basica de redireccionamiento

"""
Estructura del Path:
    path(' Nombre de la URL ', views.' Nombre de la interfaz ', name=)
"""
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='inventario'),
    path('tabla_pastel', views.tabla_pastel, name='tabla_pastel'),
    path('ingresar_nuevo_pastel', views.ingresar_nuevo_pastel, name='ingresar_nuevo_pastel'),
]