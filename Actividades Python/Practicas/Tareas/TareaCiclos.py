#Creacion de programa Creacion de Ciclos
"""
1. Solicite al usuario que ingrese un 
texto (cualquiera).
2. Solicite después al usuario ingresar 
cuántas veces desea imprimirlo (e.g. 10).

Recuerda que el programa debe imprimir el 
texto ingresado el número de veces solicitado, y terminar
"""

#Para horrar lineas de codigo
"""texto = input("Ingresa un Texto cualquiera: ")
   numero = int(input("Ingresa un numero"))     """

print("Ingresa un Texto cualquiera")
texto = input()

while True:
    print("Cuantas Veces quieres Reperir tu Texto")
    veces = int(input())
    break
    
for x in range(veces):
    print(texto)