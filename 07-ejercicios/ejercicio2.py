"""
Ejercicio 2.

Escribir un script que nos muestre por pantalla todos los numeros
pares del 1 al 120
"""

contador = 1

while contador <= 120:
    if contador % 2 == 0:
        print("Bucle while",contador)
    contador+=1

for numero in range (1,121):
    if numero % 2 == 0:
        print("Bucle for", numero)