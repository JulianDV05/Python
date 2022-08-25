from io import open #Creación

archivo_texto=open("archivo.txt", "a")#Apertura

archivo_texto.write("\n'Siempre es una buena ocasion para estudiar python'")

archivo_texto.close()