from coche import Coche

carro1= Coche("Gris","Renault","Clio",150,200,5)
carro2 = Coche("Blanco","Renault","Megane",180,250,5)
carro3 = Coche("Naranja","Renault","Arkana",220,300,5)
carro4 = Coche("Negro","Seat","Leon",170,110,5)


print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

#Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto de tipo coche")
else:
    print("No es un objeto!")

#Visibilidad
print(carro1.soy_publico)
print(carro1.getPrivado())