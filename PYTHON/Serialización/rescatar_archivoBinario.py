import pickle

fichero_rescate=open("lista_nombres", "rb")

lista=pickle.load(fichero_rescate)

print(lista)