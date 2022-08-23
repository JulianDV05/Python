from ast import Num


lista=[]

nom=input("Digite su nombre: ")
lista.append(nom)
Direc=input("Digite su dirección: ")
lista.append(Direc)
Tfno=int(input("Digite su número de teléfono: "))
lista.append(Tfno)

print(f"Los datod personales son: {lista}" )