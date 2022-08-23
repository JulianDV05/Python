print("Asignaturas optativas 2021")
print("Asignaturas operativas: \nInformática gráfica - Pruebas de Software - Usabilidad y accesibilidad")

opcion=input("\nEscribe la asignatura escogida: ")
asignatura= opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print(f"Asignatura elegida: {asignatura}")
else:
    print("La asignatura escogida no corresponde.") 