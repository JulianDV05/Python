#from typing_extensions import Self


class Coche():

    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.enmarcha and chequeo):
            return"El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return"Algo salió mal en el chequeo. No podemos arrancar"
        else:
            return"El coche está parado"

    def estado(self):
        print(
            f"El coche tiene {self.__ruedas} ruedas. \nUn ancho de {self.__anchoChasis}. \nLargo de {self.__largoChasis}")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True

        else:
            return False


miCoche = Coche()

#print(f"El largo del coche es: {miCoche.largoChasis}")
#print(f"El coche tiene: {miCoche.ruedas} ruedas")
print(miCoche.arrancar(True))

print(miCoche.estado())

print("-----------A continuación creamos el segundo objeto--------------------")

micoche2 = Coche()
#print(f"El largo del coche es: {miCoche.largoChasis}")
#print(f"El coche tiene: {miCoche.ruedas} ruedas")
print(micoche2.arrancar(False))
print(micoche2.estado())
