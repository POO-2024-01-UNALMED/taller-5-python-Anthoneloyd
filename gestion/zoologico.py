class Zoologico:
    _zonas = []
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cantidad = 0
        for zona in self._zonas:
            cantidad += zona.cantidadAnimales()

        return cantidad

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion
    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getZona(self):
        return self._zonas
    def setZona(self, zona):
        sef._zonas = zona