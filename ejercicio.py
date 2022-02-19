"""
1. Cree una clase de Persona con atributos: nombre y edad.
2. Cree un método saludar() que salude con el nombre y la edad de un objeto creado a través de la clase Persona.
3. Cree una clase secundaria Trabajador que herede de la clase Persona y que también tenga un atributo de "profesion".
4. Cree un método mostrar_trabajador() que muestre el nombre, la edad y la sección de un objeto creado a través de la clase Trabajador.
5. Cree un objeto de estudiante a través de una instanciación en la clase Trabjador y luego pruebe el método mostrar_trabajador.
"""


""" class Person:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad= edad

    def saludar(self):
        if self.nombre=='Sofia':
            print(f'Hola {self.nombre}. Cómo has estado?. Feliz cumpleaños numero {self.edad}')
        if self.nombre=='Marta':
            print(f'Hola Amiga. Felices {self.edad}')

amiga= Person('Marta','50')
visitante= Person('Sofia', 9)

amiga.saludar()
visitante.saludar() """

class Worker():
    def __init__(self,nombre,edad,seccion):
        self.nombre=nombre
        self.edad=edad
        self.seccion=seccion

    def mostrar_trabajador(self):
        if self.seccion == "Ingeniero":
            print(f'Bienvenido {self.nombre}, en que le podemos ayudar a su facultad?')

estudiante =Worker('Arturo',27,'Ingeniero')
estudiante.mostrar_trabajador()



