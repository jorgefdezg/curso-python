"""
#FOR

for variable in elemento iterable (lista,rango,etc)
    BLOQUE DE INSTRUCCIONES

"""
resultado = 0

for contador in range(0,10):
    print("Voy por el ",contador)
    resultado += contador

print("El resultado de sumar los elementos es",resultado)

#Ejemplo tablas de multiplicar
print("\n############ Ejemplo ############")

numero_usuario =int(input("De que numero quieres ver la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(1,11):

    if numero_usuario == 45:
        print("NO se pueden mostrar numeros prohibidos")
        break
    
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")