import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nPerfecto, vamos a registrarte en el sistema...")
        nombre = input("Escribe aquí tu nombre: ")
        apellidos = input("Escribe aquí tus apellidos: ")
        email = input("Escribe aquí tu email: ")
        password = input("Escribe aquí tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te has registrado correctamente!!")

    def login(self):
        print("\nPerfecto, identificate en el sistema... ")

        try:

            email = input("Escribe aquí tu email: ")
            password = input("Escribe aquí tu contraseña: ")

            usuario = modelo.Usuario("","",email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Te has identificado correctamente {login[1]}!!")
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")

    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta pronto {usuario[1]}!!")
            exit()

        return None