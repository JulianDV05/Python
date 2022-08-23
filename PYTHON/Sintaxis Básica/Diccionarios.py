diccionario={"Alemania":"Berlín","Francia":"Paris","Reino Unido":"Londres","Colombia":"Bogotá"}
print(diccionario["Alemania"])
print(diccionario)
diccionario["Italia"]="Roma"
print(diccionario)
del diccionario["Reino Unido"]
print(diccionario)

tupla=["Colombia", "Francia", "Reino Unido", "Alemania"]
diccionario={tupla[0]:"Bogotá", tupla[1]:"Paris", tupla[2]:"Londres", tupla[3]:"Berlín"}
print(diccionario)