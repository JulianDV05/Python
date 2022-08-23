def evaluaEdad(edad):

    if edad<0:
        #raise TypeError("No se permiten edades negativas")
        raise ZeroDivisionError("No se permiten edades negativas")
    if edad<20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad<65:
        return "Eres Adulto"
    elif edad<100:
        return"Cuídate"
    else:
        return "Edad errónea"

print(evaluaEdad(-15))