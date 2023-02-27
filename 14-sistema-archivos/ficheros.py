from io import open
import pathlib
import shutil
import os

#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

#Escribir
archivo.write("\n***** Soy un texto metido desde Python *****")


#Cerrar archivo
archivo.close()


#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r")

#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    # lista_frase = frase.split()
    # print(lista_frase)
    print("-"+frase.center(100))


#Copiar archivo
# ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
# ruta_alternativa = str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado88.txt"

# shutil.copyfile(ruta_original,ruta_alternativa)


#Mover archivo
# ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

# shutil.move(ruta_original,ruta_nueva)


#Eliminar archivos
# ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"
# os.remove(ruta_nueva)


#Comprobar si existe archivo
# print(os.path.abspath("../"))

if os.path.isfile(os.path.abspath("./") + "/fichero_texto55.txt"):
    print("El arhivo existe")
else:
    print("El archivo no existe")