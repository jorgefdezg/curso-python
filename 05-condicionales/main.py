#Condicional if
#Ejemplo 1
print("############# Ejemplo 1 ################")
color = "rojo"
#color =input("Adivina cual es mi color favorito: ")
if color == "rojo":
    print("Correcto!")
else:
    print("Has fallado!")


#Operadores de comparacion
#Ejemplo 2
print("\n############# Ejemplo 2 ################")
year = 2020
#year = int(input("En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


#Ejemplo 3
print("\n############# Ejemplo 3 ################")

nombre = "Jorge"
ciudad = "Vilagarcia"
continente = "Asia"
edad = 26
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Europa":
        print("El usuario no es europeo")
    else:
        print(f"{nombre} es europeo, de la ciudad de {ciudad}")

else:
    print(f"{nombre} no es mayor de edad")


#Ejemplo 4
print("\n############# Ejemplo 4 ################")
dia = 2
#dia = int(input("Introduce el numero del día de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia ==2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")


#Ejemplo 5
print("\n############# Ejemplo 5 ################")

edad_minima = 18
edad_maxima = 65
edad = 26
#edad = int(input("Indica tu edad: "))
if edad >= 18 and edad <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")


#Ejemplo 6
print("\n############# Ejemplo 6 ################")

pais = "Colombia"

if pais == "España" or pais == "Colombia" or pais == "Mexico":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")


#Ejemplo 7
print("\n############# Ejemplo 7 ################")

pais = "España"

if not(pais == "España" or pais == "Colombia" or pais == "Mexico"):
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")


#Ejemplo 8
print("\n############# Ejemplo 8 ################")

pais = "USA"

if pais != "España" and pais != "Colombia" and pais != "Mexico":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")