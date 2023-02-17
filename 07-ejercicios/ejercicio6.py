"""
Vamos a mostrar todas las tablas de multiplicar del 1 al 10
"""

for numero in range(1,11):
    print(f"\nTabla de multiplicar del {numero}")
    for numero2 in range(1,11):
        print(f"{numero} x {numero2} = {numero*numero2}")