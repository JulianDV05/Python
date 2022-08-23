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