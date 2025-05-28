#Creacion de listas en Python
#Los indices comienzan por el Indice 0, seguido del Indice 2 y asi 
#Las listas son Modificables
nombres = ["Jaime", "Juan", "Pedro"]
print(nombres[0])

#Aqui modificamos la lista, cambiamos el nombre Juan, por un nomnbre de David
"""Para esto tenemos que llamarlo por su indice 
nombre de la lista[numero del indice que quieras modificar] = Dato nuevo modificado"""
nombres[1] = "David"
print(nombres[1])

#Funciones de una lista
"""Imprimir la longitud de la lista, cuentos elementos tiene la lista
print(len/longitud(nombre de la lista))"""
print(len(nombres))

#Tipo de datos que tiene la lista
""" Podemos mirar que tipos de datos tiene una lista
print(type/ tipo de dato(nombre de la lista))"""
print(type(nombres))

#Agregar datos nuevos a la lista = Funcion (append)
"""El elemento (append) nos sirve para agregar un elemento nuevo al final de la lista
nombre de la lista .append(Funcion para agregar dato)("Dato nuevo")"""
nombres.append("Andujo")
print(nombres)

#Funcion para quitar un elemento de la lista
"""El elemento (.remove) nos sirve para poder elimimnar un elemto de la lista
nombre de la lista .remove(Funcion para Eliminar dato)("Dato a eliminar")"""
nombres.remove("Pedro")
print(nombres)

#Otra manera para eliminar un elemento utilizando el Indice
"""En este caso para poder eliminar un elemento de la lista es utilizando el indice
del (palabra para poder eliminar elemento) nombre de la lista [Indice que deseas eliminnar]"""
del nombres[1]
print(nombres)

#Tambien podemos saber si un dato esta en una lista
"""Esta es una expresion, que revisa la lista
mostrara un tipo boolean, True / False, en este caso Mostrara True, ya que el valor que buscamos SI esta en la lista"""
print("Jaime" in nombres)

"""En este caso Mostrara False, ya que el valor que buscamos NO esta en la lista"""
print("Pepe" in nombres)

#Boptener secciones de la lista
"""En caso de tener mas valores, podemos buscarlos"""
nombre = ["Jaime", "Juan", "Pedro", "Antonio", "Andujo", "Lucero", "Diana", "Guadalupe"]
print(nombre)

#Primera Forma
"""Imprimimos ((Podemos colocar un comentario), nombre de la lista [Indice de donde quiero iniciar : Indice de donde deje de mostrar])
de igual forma aca, podemos seleccionar desde donde podemos seleccionar los datos de la lista"""
print("Bienvenidos a la fiesta", nombre [:3])

"""En esta parte del codigo, mostramos un comentario donde mencionamos un caso cualquiera, seleccionamos una lista y colocamos que queremos
seleccionar de ella, en este caso le desimos que desde el indice 3 en adelante muestre los demas datos de la lista, se le coloca el ( : ) seguido
de el no se coloca nada, ya que queremso que muestre los demas datos de la tabla, asi no colocamos ningun otro numero"""
print("Lo sentimos", nombre [3:])

#Podemos iterar a todos los datos de una lista
"""Iteracion tipo FOR
La letra N es por asi decirlo, cada dato de la lista. Utilizamos
    for (Nombre de una variable que mostrara, cada dato de la lista) in (Nombre de la lista):
        print("Comentario / Opcional" , n )"""
for n in nombre:
    print("Se unio a la lista", n)

"""No puedes utilizar los indices ya que necesitamos una funcion llamada (Enumerate).
En este caso, lo que estamos haciendo es mostrar los datos de la lista y tambien mostra que indice tiene cada valor de la lista
Asi:
    Se unio a la lista: 0(Numero de indice) Jaime (Dato de la lista)
    Se unio a la lista: 1(Numero de indice) Juan (Dato de la lista)
    Se unio a la lista: 2(Numero de indice) Pedro (Dato de la lista)
Asi, hasta mostrar cada dato de la lista, con su respectivo indice""" 
for i, n in enumerate(nombre):
    print("Se unio a la lista", i, n)
    
#Formateo elegante de TEXTOS / f-string
for i, nombre in enumerate(nombre):
    print( f"Se unio a la fiesta {nombre} y esta en el asiento {i}" )