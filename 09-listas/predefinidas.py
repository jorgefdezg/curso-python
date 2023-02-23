cantantes = ["2pac","Drake","Bad Bunny","Julio Iglesias"]
numeros = [1,2,5,8,3,4]


#Ordenar
# print(numeros)
numeros.sort()
# print(numeros)


#Añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1,"David Bisbal")
print(cantantes)


#Eliminar elementos
cantantes.pop(1)
cantantes.remove("Drake")
# print(cantantes)


#Dar la vuelta
numeros.reverse()
#print(numeros)


#Buscar dentro de una lista
print("2pac" in cantantes)


#Contar elementos
print(cantantes)
print(len(cantantes))


#Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))


#Conseguir indice
print(cantantes.index("2pac"))


#Unir listas
cantantes.extend(numeros)
print(cantantes)