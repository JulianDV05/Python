edad=int(input("Introduzca la edad por favor: "))

while edad<5 or edad>100:
    print("Introdujo una edad negativa. Por favor vuelva a intentarlo.")
    edad=int(input("\nIntroduzca la edad por favor: "))

print("\nGracias, puedes pasar.")
print(f"Edad del aspirante: {edad}")