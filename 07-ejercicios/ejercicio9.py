"""
Ejercicio 9.

Mientras que el usuario no meta el 111, el programa seguirá pidiendo numeros
y mostrandolos
"""
numero = int(input("Adivina el numero en el que estoy pensando: "))
while numero != 111:
    print(f"Error! No estoy pensando en el {numero}")
    numero = int(input("Adivina el numero en el que estoy pensando: "))

print(f"Has acertado, el numero era el {numero}")