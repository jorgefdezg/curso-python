#Programacion orientada a objectos (POO)

#Definir una clase (molde para crear objetos de ese tipo)
#Coche con caracteristicas similares

class Coche:

    #Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos, son acciones que hace el objeto(coche)
    def setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

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
    
#Fin definicion clase

#Crear objetos / Instanciar clase

coche = Coche()

coche.setColor("amarillo")
coche.setModelo("458")
print("Coche 1:")
print(coche.getMarca(), coche.getModelo(),coche.getColor())
print("Velocidad actual:", coche.getVelocidad())

coche.frenar()

print("Velocidad post-frenada",coche.getVelocidad())
print("-----------------------------")
#Crear mas objetos
coche2 = Coche()
coche2.setMarca("Seat")
coche2.setModelo("Ibiza")
coche2.setColor("Verde")

print("Coche 2:")
print(coche2.getMarca(), coche2.getModelo(),coche2.getColor())

print(type(coche2))