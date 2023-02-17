"""
Ejercicio 3.

Escribir un programa que muestre los cuadrados de los primeros 60
numeros naturales.
"""
contador = 1

for numero in range (1,61):
    print(f"El numero {numero} elevado al cuadrado es igual a {numero*numero}")

while contador <=60:
    print(f"El numero {contador} elevado al cuadrado es igual a {contador*contador}")
    contador+=1