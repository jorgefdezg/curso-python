"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla.
- Hacer una funcion que recorra listas de numeros y devuelva un string
- Ordenar la lista y mostrarla.
- Mostrar su longitud
- Buscar un elemento que el usuario pida por teclado.
"""

numeros = [8,12,3,9,1,33,11,6]

def mostrarLista(numeros):
    lista = ""
    tamano = len(numeros)
    iterador = 1
    for numero in numeros:
        lista+=str(numero)
        if tamano != iterador:
            lista+=","
            iterador+=1
    return lista

lista = mostrarLista(numeros)
print(lista)
numeros.sort()
print(f"Lista ordenada {numeros}")
print(f"Longitud de la lista = {len(numeros)}")

numero = int(input("Escriba el numero que desea buscar: "))
busqueda = numeros.index(numero)
print(f"El numero buscado existe en la lista, es el indice {busqueda}")