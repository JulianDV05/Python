class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")


class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculos):
    hacecaballito = ""

    def caballito(self):
        self.hacecaballito = "Voy haciendo caballito"

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \nHace caballito: {self.hacecaballito}")


class VElectricos(Vehiculos):
    def __init__(self):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

