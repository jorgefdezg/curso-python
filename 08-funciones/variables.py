"""
Variables locales: Se definen dentro de la funcion y no se
pueden usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return

Variables globales: Son las que se declaran fuera de la funcion y
estan disponibles dentro y fuera de ellas.
"""

#Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    global mail
    mail = "jorge.fernandez3@udc.es"
    print("Dentro:",mail)
    return year

year = holaMundo()
print(f"Estamos en el año {year}")
print(f"El mail es : {mail}")