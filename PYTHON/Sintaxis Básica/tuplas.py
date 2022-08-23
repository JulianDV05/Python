#Cuando no se ponen parentesis, también es una tupla y se conoce como empaquetado de tupla
tupla=("Juan", 13,1,1995,13)
print(tupla[1])

lista=list(tupla)
print(lista)

print("Juan" in lista)

print(tupla.count(13))

print(len(tupla))

#Lo siguiente se le conoce como desempaquetado de tupla.
nombre, edad, ide, año, numero=tupla
print(nombre)
print(edad)
print(ide)
print(año)
print(numero)
