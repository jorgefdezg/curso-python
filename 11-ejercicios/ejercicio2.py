"""
Ejercicio 2.
Escribir un programa que añada valores a una lista mientras
que su longitud sea menor a 120 y luego mostrar esa lista.
Plus: Usar while y for.
"""

lista = []
contador = 0

# for elemento in range(0,120):
#     lista.append(elemento)

# print(lista)

while len(lista) < 120:
    lista.append(contador)
    contador+=1

print(lista)
