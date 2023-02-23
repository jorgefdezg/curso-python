"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a la funcion
tantas veces como sea necesario.

def nombreFuncion(parametros):
    #Conjunto de instrucciones

nombreFuncion(mi_parametro)

"""

#Ejemplo 1
print("####### Ejemplo 1 #######")

#Definimos la funcion
def muestraNombre():
    print("Jorge")
    print("Samuel")
    print("Alejandro")
    print("Pablo")
    print("Laura")
    print("\n")

#Invocamos a la funcion
muestraNombre()
muestraNombre()
muestraNombre()

#Ejemplo 2
print("####### Ejemplo 2 #######")

def mostrarTuNombre(nombre,edad):
    print("Tu nombre es:",nombre)

    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Y eres mayor de edad")

# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))
# mostrarTuNombre(nombre,edad)


#Ejemplo 3
print("####### Ejemplo 3 #######")

def tablaMultiplicar(numero):
    print(f"Tabla de multiplicar del número {numero}")
    for contador in range (1,11):
        print(f"{numero} x {contador} = {numero*contador}")
    
    print("\n")

# numero = int(input("Introduce el numero del que quieres saber su tabla de multiplicar: "))
# tablaMultiplicar(numero)

for numero_tabla in range(1,11):
    tablaMultiplicar(numero_tabla)


#Ejemplo 4
print("####### Ejemplo 4 #######")

#Parametros opcionales
def getEmpleado(nombre, dni = False):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != False and dni != None:
        print(f"DNI: {dni}")

getEmpleado("Jorge","2222222")


#Ejemplo 5
print("####### Ejemplo 5 #######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo
print(saludame("Jorge"))


#Ejemplo 6
print("\n####### Ejemplo 6 #######")

def calculadora(numero1,numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(5,5))


#Ejemplo 7
print("\n####### Ejemplo 7 #######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Jorge", "Fernandez"))


#Ejemplo 8 Funciones lambda
print("\n####### Ejemplo 8 #######")

dime_el_anho = lambda year: f"El año es {year}"

print(dime_el_anho(2022))