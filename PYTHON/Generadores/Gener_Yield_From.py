def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento


ciudades_devueltas = devuelve_ciudades("Madrid", "Ibagué", "Barcelona", "Bogotá", "Medellín")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))