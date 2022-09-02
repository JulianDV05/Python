from io import open

archico_texto = open("archivo.txt", "r")
#archico_texto.seek(11)
print(archico_texto.read(11))
print(archico_texto.read())