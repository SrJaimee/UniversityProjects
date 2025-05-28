print("Escribe tu nombre")
nombre = input()
print("Escribe tu edad")
edad = int(input())


#elif // De lo contrario
#Operadores logicos
#and (Y) // or (O)
# > < >= <=
if nombre == "Jaime" and edad >= 20:
    print("Saludos Jaime, eres un adulto")
elif nombre == "Jaime" and edad < 20:
    print("Saludos Jaime, eres un joven")
else:
    print("Saludos")
    
#Utilizando el (OR)
if nombre == "Jaime" or nombre == "David":
    print("Me gusta tu nombre")
else:
  print("Que nombre tan extrano")   
