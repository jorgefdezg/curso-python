"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
"""

from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")
accion = acciones.Acciones()

eleccion = input("¿Que quieres hacer?: ")

if eleccion == "registro":
    accion.registro()

elif eleccion == "login":
    accion.login()
