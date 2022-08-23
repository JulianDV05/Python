from coche import Coche, CocheDeportivo
#from coche import CocheDeportivo / Esta no sería la mejor manera
#mport coche / => Así se importaría todo el fichero

coche1 = Coche("SEAT", "Negro")
print(f"Marca: {coche1.marca}, Color: {coche1.color}")

coche_lujo = CocheDeportivo("BMW", "Rojo", 130)
print(f"\nMarca: {coche_lujo.marca}\n Color: {coche_lujo.color}\n Caballos Fuerza: {coche_lujo.cf}")