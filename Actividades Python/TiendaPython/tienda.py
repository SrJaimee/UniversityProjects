from datetime import datetime

print("""
***************************************
**           Bienvenido a la         **
**         Tienda de Mascotas        **
***************************************
""")


num_perros = 10
num_gatos = 8
num_pajaros = 25
animales_totales = num_perros + num_gatos + num_pajaros

nombre = input("Ingresa tu Nombre: ")
apellido = input("Ingrese su Apellido: ")

nombre_completo = nombre + " " + apellido
print("Gracias por visitarnos, ", nombre_completo)

compras = []

def mostrar_menu():
    print("""
================================================
Selecciona la opcion que deseas:
1: Conocer cuantos animales tiene la tienda
2: Adoptar una mascota
3: Mostrar compras
4: Salir de la tienda 
""")
    
def mostrar_inventario():
    print("Actualmente contamos con:")
    print(f"Perros: {num_perros} Gatos: {num_gatos} Pajaros: {num_pajaros}")
    print(f"En total tenemos: {animales_totales} animales")

def adoptar():
    carrito = []
    while True:
        print("Que mascota quieres adoptar? solo puedes adoptar un Animal de una especie")
        print("Presiona (x) para salir del Carrito, presiona (v) para mirar tu Carrito")
        animal = input()
        if animal == "x":
            break
        if animal == "v":
            print(f"Tu estas adoptando a {carrito}")
            continue
        if animal not in carrito:
            carrito.append(animal)
        else:
            print("Ese animal ya lo adoptaste")

    print("El contenido de tu carrito es: ")
    for animal in carrito:
        print("     ", animal)
    
    fecha = datetime.now()
    compras.append( (nombre, carrito, fecha))
        
def mostrar_Compras():
    print("")
    print("*********** Compras Realizadas ***********")
    for compra in compras:
        print(f"    {compra[0]} compro {compra[1]} en {compra[2]}") 
    
while True:
    mostrar_menu()
    respuesta = int(input())
    if respuesta == 1:
        mostrar_inventario()
    elif respuesta == 2:
        adoptar()
    elif respuesta == 3:
        mostrar_Compras()
    elif respuesta == 4:
        print("Saliendo de la tienda")
        break
    
#Holaaa