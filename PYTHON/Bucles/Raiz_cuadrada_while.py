import math


print("Programa de cálculo de raiz cuadrada.")
numero=int(input("Introduzca el número por favor: "))

intentos=0

while numero < 0:
    print("No se puede hallar la raiz de un número negativo")

    if intentos==2:
        print("Limite de intentos. \nEl programa ha finalizado.")
        break;
    
    numero=int(input("Introduzca un número por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos <2:
    solucion=math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")