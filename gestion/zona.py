class Zona:
    def __init__(self, nombre = None, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo
    def setZoo(self, zoo):
        self._zoo = zoo