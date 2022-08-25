from io import open #Creación

archivo_texto=open("archivo.txt", "w")#Apertura

frase="Estupendo día para estudiar python \nel martes" 
archivo_texto.write(frase)#Manipulación

archivo_texto.close()#Cerrarlo