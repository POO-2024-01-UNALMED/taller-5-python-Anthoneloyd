class Animal:
    _totalAnimales = 0
    _zona = None

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self._totalAnimales += 1

    def movimiento ():
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        return ("Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) +
                "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) +
                "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) +
                "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) +
                "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios()))

    def toString(self):
        if self._zona == None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona.getNombre() + ", en el zoo " + self._zona.getZoo().getNombre()


    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero