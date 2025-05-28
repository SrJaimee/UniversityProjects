#Creacion de la Tarea N.1
"""
Crea un programa que imprima un mensaje solicitando al 
usuario un número entre el 1 y el 100:

a) Si el número es menor a 1, debe imprimir un mensaje 
“Favor de ingresar un número mayor a 0”.
b) Si el número es mayor a 100, debe imprimir un mensaje 
“Favor de ingresar un número menor o igual a 100”.
c) Si el número sí es entre 1 y 100, debe imprimir un 
mensaje “¡Muy bien! El <número> es una gran opción.
"""

print("Elige un Numero del 1 al 100")
num = int(input())

if num <= 0:
     print("Favor de ingresar un número mayor a 0")
elif num >= 100:
    print("Favor de ingresar un número menor o igual a 100")
else:
    print(f"¡Muy bien! El {num} es una gran opción")
