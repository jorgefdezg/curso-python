"""
Ejercicio 7.
Hacer un programa que muestre todos los numeros impares entre
dos numeros escogidos por el usuario.
"""

numero_1 = int(input("Escoja el primer numero: "))
numero_2 = int(input("Escoja el segundo numero: "))

if numero_1 < numero_2:
    for numero in range(numero_1,numero_2+1):
        if numero % 2 != 0:
            print(numero)
else:
    for numero in range(numero_2,numero_1+1):
        if numero % 2 != 0:
            print(numero)