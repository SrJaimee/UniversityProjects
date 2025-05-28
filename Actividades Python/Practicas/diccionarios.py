#Creacion de un Diccionario
# #Una lista de elemento llave: valor
#Arreglos asociativos

"""Estructura de un diccionario:
Nombre del diccionario = {"llave": "Valor",
                          "llave": "Valor",
                          "llave": "valor"}
                          
Nombre del diccionario = {"llave": "Valor", "llave": "Valor","llave": "valor"}           
           
Para poder llamar algun dato del diccionario, debemos de 
utilizar su llave
                    print(Nombre del diccionario ["AQUI LLAVE"])
De esta manera, accedes al dato de la biblioteca

Los diccionarios si son modificables, pero no se acumulan los valores
Esto lo que realiza, es ir a buscar la llave y poder modificarla, no se 
modifica la llave, se modifica el dato
"""
persona = {"Nombre": "Jaime",
           "Edad" : 21, 
           "Apellido": "Andujo"}

#Poder agregar una llave nueva al diccionario
persona["Apodo"] = "Jimmy"

persona["Apellido"] = "Paredes"
print(persona["Apellido"])
print(persona)

#Como obtener una lista de todas las llaves del diccionario, estructura de los datos

print(persona.keys())