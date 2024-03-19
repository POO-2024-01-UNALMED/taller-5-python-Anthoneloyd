class Ave(Animal):
    _listado = []

    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def cantidadAves():
        return len(Ave._listado)

    def movimiento():
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montaña", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montaña", genero, "blanco y amarillo")

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas