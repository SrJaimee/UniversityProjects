3#Creacion de Ciclos // Iteracion // Bucle
#Sentencias // While // For
#ctrl + c // Para parar la consola

#Ciclo while // Exprecion a True // while <expresion>
#While == Mientras
i = 0
while i < 10:
    if i < 5:
            print("El numero", i ,"es menor que 5")
    else:
        print("El numero", i ,"es mayor o igual a 5")
    i += 1
print("Termino la iteracion")

#Ciclo For
#Ciclo For// (Por) cada X (en) "Jaime", cada letra es una X 
for x in "Jaime":
    print(x)

#Funcion Range
for x in range(1, 10):
    print(x)

#Break // Se utiliza para poder salir de interaciones
#cuando se cumple alguna conducion que nosotros queremos
while True:
    print("Escribe tu opcion")
    print("1. Entrar")
    print("2. Salir")
    respuesta = int(input())
    
    if respuesta == 1:
        print("Hola, amigo mio")
    elif respuesta == 2:
        break     
print("Terminando programa")
