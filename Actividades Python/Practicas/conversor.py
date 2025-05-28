#Practica para que el Usuario ingrese datos

print("Bienvenido al conversor de millas a kilometros")

#Para pedir informacion al usuario
print("Escribe un numero en Millas: ")
millas = input() #Siempre muestra un string

#En esta parte la varible Millas es tipo string, lo tenemos que cambiar a tipo Numero o flotante
print("Tipo de datos de millas", type(millas))

#Convertir de string a numero
#Aqui se combirtio en flotante
millas = float(millas)
print("Tipo de datos de millas", type(millas))

#Formula (1 milla = 1.609)
kilometros = millas * 1.609

print("Millas ingresadas:", millas)
print("Kilometros:", kilometros)