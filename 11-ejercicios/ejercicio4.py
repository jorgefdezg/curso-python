"""
Ejercicio 4.
Crear un script que tenga 4 variables, una de tipo lista, otra de tipo entero
otra de tipo booleano y otra de tipo string y que imprima un mensaje
segun el tipo de dato de cada variable
"""

lista = [1,2,4,5]
texto = "hola que tal"
numero = 33
booleano = True

def comprobarTipo(dato):
    tipo = type(dato)
    print(f"El dato {dato} es un {tipo}")

comprobarTipo(numero)