#Creacion de una tienda de Manzanas
#Intento uno
print("Bienvenido a la tienda de Manzanas")
print("Escribe tu Nombre")
nombre = input()

manzanas = 20
precio = 5

print("Hola,", nombre, ". Actualmente tenemos", manzanas, "manzanas disponibles, con un precio de", precio, "pesos")

print("Cuantas manzanas quieres comprar?")
comprar = input()
comprar = int(comprar)
total = comprar * precio

print("Compro", comprar, "manzanas, el precio a pagar es:", total)

Man_Restantes = manzanas - comprar
print("Manzanas disponibles despues de la compra son", Man_Restantes)
