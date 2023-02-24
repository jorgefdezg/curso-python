"""
Modulos: Funcionalidades ya hechas para reutilizar.
En python hay muchos modulos, que los puedes consultar en su
pagina web.

Podemos conseguir modulos que ya vienen en el lenguaje,
conseguir en internet o crearlos nosotros mismos.
"""

#Importar modulo propio
#import mimodulo
from mimodulo import *

print(holaMundo("Jorge"))
print(calculadora(3,5,False))


#Modulo fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y,%H:%M:%S")
print(fecha_personalizada)

print(datetime.datetime.now().time())


#Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ",float(math.pi))

print("Redondear: ", math.ceil(6.56789))

print("Redondear a la baja: ", math.floor(6.6789))


#Modulo random
import random

print("Numero aleatorio entre 15 y 67: ",random.randint(15,67))

