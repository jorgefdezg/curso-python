import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"Vale {usuario[1]}, vamos a crear una nueva nota!")

        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("\nIntroduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0],titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print("La nota se ha guardado correctamente!")
        
        else:
            print(f"No se ha guardado la nota, lo siento {usuario[1]}")

    
    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]}!. Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n-------------------------------------")
            print("Titulo:",nota[2])
            print("\nDescripcion:"+"\n",nota[3])
            print("\n-------------------------------------")



    def borrar(self,usuario):
        print(f"\n Hola {usuario[1]}, vamos a borrar notas:")

        titulo = input("Introduce el titulo de la nota que deseas eliminar: ") 

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota: {nota.titulo}")

        else:
            print("No se ha borrado la nota")