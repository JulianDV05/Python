class Persona():
    def __init__(self, nombre, edad, ciudad_residencia):

        self.nombre = nombre
        self.edad = edad
        self.ciudad_residencia = ciudad_residencia

    def descripcion(self):

        print(
            f"Nombre: {self.nombre}, Edad: {self.edad}, Residencia: {self.ciudad_residencia}")


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, ciudad_empleado):

        super().__init__(nombre_empleado, edad_empleado, ciudad_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()

        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}")


Antonio = Empleado(1500000, 10, "Antonio", 55, "Colombia")

Antonio.descripcion()

print(isinstance(Antonio, Persona))
