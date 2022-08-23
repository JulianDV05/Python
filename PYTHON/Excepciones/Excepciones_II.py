def divide():

    try:
        op1= float(input("Introduzca el primer número: "))
        op2= float(input("Introduce el segundo número: "))

        print(f"La division es: {op1/op2}")

    except ValueError:
        print("El valor introducido es erróneo")
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")  

    finally:
        print("Cálculo finalizado")

divide()