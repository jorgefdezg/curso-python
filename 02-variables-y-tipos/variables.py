"""
Una variable es un contenedor de información que
dentro guardará un dato, se pueden crear muchas variables
y que cada una tenga un dato distinto.
"""

#Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "Con Victor Robles"
numero = 45
decimal = 6.7

#Mostrar variables
print(texto)
print(texto2)
print(numero)
print(decimal)

#Reasignar valores
numero = 77
decimal = 8.9

#Mostrar valor cambiado
print("---------------------------------------")
print(decimal)
print(numero)
print("---------------------------------------")

#Concatenacion
nombre = "Jorge"
apellidos = "Fernandez"
web = "https://github.com/jorgefdezg"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es {}".format(nombre,apellidos,web))

print(nombre,apellidos,web)