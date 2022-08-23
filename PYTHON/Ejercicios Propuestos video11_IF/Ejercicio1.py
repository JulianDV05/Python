num1=float(input("Introduzca un número: "))
num2=float(input("Introduzca otro número: "))

def DevuelveMax(num1,num2):
    if num1>num2:
        print(f"El numero mayor es {num1}")
    elif num2>num1: 
        print(f"El numero mayor es {num2}")
    else:
        print("Los numeros son iguales")

DevuelveMax(num1,num2)
