"""
Listas
Son colecciones o conjuntos de datos/valores, bajo un
unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"
#Definir lista
peliculas = ["Batman","Spiderman","El señor de los anillos"]
cantantes = list(("Drake","Eminem","Nicki Minaj"))
years = list(range(2020,2050))
variada = ["Victor",30,5.5,True,"Texto"]

# print(pelicula)
# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)


#Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

pelicula = "Origen"
peliculas[1] = pelicula
print(peliculas)

#Añadir elementos a la lista
cantantes.append("Laura Pausini")
print(cantantes)
cantantes.append("Kaze")
print(cantantes)


#Recorrer una lista
nueva_pelicula = ""

# while nueva_pelicula != "parar":
#     nueva_pelicula = input("Introduce la nueva pelicula: ")
#     if nueva_pelicula != "parar":
#         peliculas.append(nueva_pelicula)

print("\n Mostrando peliculas guardadas")
for elemento in peliculas:
    print(f"{peliculas.index(elemento)+1}. {elemento}")


#Listas multidimensionales
print("\n ***** Lista de contactos *****")
contactos = [
    [
        "Jorge",
        "jorge.fernandez3@udc.es"
    ],
    [
        "Manuel",
        "manolo.perez@usc.es"
    ],
    [
        "Jacobo",
        "jacobo.rodriguez@uvigo.es"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: ",elemento)
        else:
            print("Email: ",elemento)
    print("\n")

#print(contactos[1][1])