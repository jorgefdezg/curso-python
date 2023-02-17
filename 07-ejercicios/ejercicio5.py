"""
Ejercicio 5.

El programa deberá mostrar todos los números entre los dos
numeros que introduce el usuario por pantalla.
"""

numero_1 = int(input("Escribe el primer numero: "))
numero_2 = int(input("Escribe el segundo numero: "))

if numero_1 < numero_2:
    for numero in range(numero_1+1,numero_2):
        print(numero)
else:
    for numero in range(numero_2+1,numero_1):
        print(numero)