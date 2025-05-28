#Creacion de Juego de dados
#Libreria Random
import random

#Creacion de dados, numeros randoms
def tirar_dados():
    return random.randint(2,12)
print("Tiro de dados:", tirar_dados())

#Creacion del Menu
def pedir_respuesta():
    print("Ingresa tu prediccion")
    print("1. Par")
    print("2. Impar")
    print("3. Salir del juego")
    return int(input())
    """
    respuesta = int(input())
    return respuesta
    """

def imprimir_resultado(numero, prediccion):
    #Logico // Modulo
    # not // %
    es_par = numero % 2 == 0
    if es_par and prediccion == 1:
        print("Ganaste, Numero de los dados:", numero)
    elif not es_par and prediccion == 2:
        print("Ganaste, Numero de los dados:", numero)
    else:
        print("Perdiste, Numero de los dados:", numero)

while True:
    numero = tirar_dados()
    prediccion = pedir_respuesta()
    if prediccion == 3:
        break
    imprimir_resultado(numero, prediccion)
    
print("Gracias por jugar")