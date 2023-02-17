"""
Ejercicio 10.

El usuario debe meter X notas de alumnos y sacar por pantalla cuantos
han aprobado y cuantos han suspendido. 
"""
alumnos = int(input("¿Cuantos alumnos hay en clase?: "))
aprobados = 0
suspensos = 0
contador = 0

while contador < alumnos:
    nota = int(input("Escriba la nota que ha sacado el alumno: "))
    if nota < 5:
        suspensos+=1
        contador+=1
    elif nota >= 5 and nota <=10:
        aprobados+=1
        contador+=1
    else:
        print("Esta nota no es valida")

print(f"Han aprobado {aprobados} alumnos, y han suspendido {suspensos} alumnos")