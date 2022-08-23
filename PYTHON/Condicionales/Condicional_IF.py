nota_alumno=int(input("Digite la nota:"))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota<5:
        valoracion  = "desaprobado"
    return valoracion


print(evaluacion(nota_alumno))