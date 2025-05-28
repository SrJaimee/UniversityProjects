#Creaciones de Funciones
#En este caso, buscaremos la longitud del dato nombre
nombre= "Jaime"
print("Longitud del nombre",  len(nombre))

#Funciones Matematicas
#abs // La funcion abs absoluto, obtiene el valor absoluto de cualquier dato del parametro
resultado = abs(-10)
print(resultado)

#Creacion de un numero Aleatorio del (1 al 100)
#Libreria // random
#randomInt // Numero aleatorio pero en Entero // Resive dos parametro 
#randint(min, max)
#Podemos usar librerias externas a Python, las podemos descargar desde la comunidad
import random
resultado_Rand = random.randint(1, 100)
print(resultado_Rand)

#Funciones con mas parametros
def saludar_y_sumar(nombre, num1, num2):
    print("Saludos", nombre)
    print("Resultado de la suma", num1+num2)
    