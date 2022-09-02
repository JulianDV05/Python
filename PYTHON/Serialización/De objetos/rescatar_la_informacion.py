import pickle
import serializar_objetos #Hay que importar el archivo para que lea el objeto Vehiculos, de lo contrario dará error.

ficheroApertura=open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for i in misCoches:
    print(i.estado())
    print()