class Coche:
    marca = ""
    color = "Blanco"
    encendido= False
    velocidad = 0

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def encender(self):
        self.encendido = True

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

coche1 = Coche("SEAT", "Negro")
#coche_lujo = Coche("BMW", "Plateado")
coche1.encender()
coche1.set_velocidad(40)

print(f"Marca: {coche1.marca}, Color: {coche1.color}")
#print(f"Marca: {coche_lujo.marca}, Color: {coche_lujo.color}")
if coche1.encendido:
    print(f"El coche está encendido y va a una velocidad de {coche1.velocidad} km/h")
    coche1.set_velocidad(120)
    print(f"El coche está encendido y va a una velocidad de {coche1.velocidad} km/h")
else:
    print("El coche está apagado")