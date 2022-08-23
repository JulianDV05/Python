from ast import Num
import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

num=int(input("Introduce un número: "))
try:
    print(calculaRaiz(num))
except ValueError as ErrorDeNumNegativo:

    print(ErrorDeNumNegativo)
    
print("Programa terminado")