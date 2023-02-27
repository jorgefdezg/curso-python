class Coche:

    #Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, soy un atributo publico"
    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self,color,marca,modelo, velocidad, caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #Metodos, son acciones que hace el objeto(coche)
    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad+= 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def setPlazas(self,plazas):
        self.plazas = plazas
    
    def getPlazas(self):
        return self.plazas
    
    def getInfo(self):

        info = "----- Informacion del coche -----"
        info+= "\n Marca: " + self.getMarca()
        info+= "\n Modelo: " + self.getModelo()
        info+= "\n Color: " + self.getColor()
        info+= "\n Velocidad: " + str(self.getVelocidad())

        return info
    
    def getPrivado(self):
        return self.__soy_privado