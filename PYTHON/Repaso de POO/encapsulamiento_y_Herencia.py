class Coche:
    marca = ""
    color = "Blanco"
    __encendido = False

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def encender(self):
        self.__encendido = True
    
    def get_encendido(self):
        return self.__encendido

class CocheDeportivo(Coche):
    cf = 60
    def __init__(self, marca, color, cf):
        super().__init__(marca, color)
        self.cf = cf

coche1 = Coche("SEAT", "Negro")
coche1.encender()
#coche1.encendido = True

print(f"Marca: {coche1.marca}, Color: {coche1.color}")
print(f"Encendido: {coche1.get_encendido}")

coche_lujo = CocheDeportivo("BMW", "Rojo", 130)
print(f"\nMarca: {coche_lujo.marca}\n Color: {coche_lujo.color}\n Caballos Fuerza: {coche_lujo.cf}")