print("Programa de becas año 2021")

distancia=float(input("Introduzca la distancia a la escuela en KM: "))
print(distancia)

hermanos=int(input("\nIntroduzca en número de hermanos con lo que vive: "))
print(hermanos)

salario=float(input("\nIntroduzca el salario anual bruto: "))
print(salario)

if distancia>40 and hermanos>2 or salario<=1000000:
    print("Tienes derecho a beca.")
else:
    print("No tienes derecho a beca.")
