#Creacion de Funciones // print // type // range
#Sabemos que son funciones, por que utilizan ( ) parentesis
#Parametro // Un parametro es una variable que una funcion puede utilizar para trabajar
#def saludar(PARAMETRO)

#Definiendo una funcion // def
def saludar(nombre):
    print("Hola", nombre)
saludar("Jaime")
saludar("Andujo")
saludar("David")

#Creacion de Celsius a Fahrenheit: (C * 1.8) + 32
def convertir_a_Fahrenheit(c):
    return (c * 1.8) + 32
print(convertir_a_Fahrenheit(15))
print(convertir_a_Fahrenheit(10))
print(convertir_a_Fahrenheit(20))