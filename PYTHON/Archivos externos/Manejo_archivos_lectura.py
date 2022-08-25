from io import open #Creación

archivo_texto=open("archivo.txt", "r")#Apertura

# texto = archivo_texto.read()

# archivo_texto.close()
# print(texto)

lineas_texto=archivo_texto.readlines()
archivo_texto.close()

print(lineas_texto)