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

class Coche4x4:
    size_ruedas = 18

class CocheDeportivo(Coche, Coche4x4):
    cf = 60
    def __init__(self, marca, color, cf, size_ruedas):
        super().__init__(marca, color)
        self.cf = cf
        self.size_ruedas = size_ruedas

coche1 = Coche("SEAT", "Negro")
print(f"Marca: {coche1.marca}, Color: {coche1.color}")

coche_lujo = CocheDeportivo("BMW", "Rojo", 130, 19)
print(f"\nMarca: {coche_lujo.marca}\n Color: {coche_lujo.color}\n Caballos Fuerza: {coche_lujo.cf}\n Tamaño Ruedas: {coche_lujo.size_ruedas}")