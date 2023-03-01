#Importar modulo
import sqlite3

#Conexion
conexion = sqlite3.connect("./19-bases-datos/pruebas.db")

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar (255),             
    descripcion text,
    precio int(255)
);
""")

#Guardar cambios
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Decripcion de mi producto', 550)")
conexion.commit()
"""

#Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC",600),
    ("Telefono movil", "Buen telefono",140),
    ("Placa base", "Buena placa",80),
    ("Tablet 15", "Buena tablet",300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio = 80;")

#Lectura de datos
cursor.execute("SELECT * FROM productos WHERE precio >=300;")
productos = cursor.fetchall()

for producto in productos:
    print("ID:",producto[0])
    print("Titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])
    print("--------------------")

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)


#Cerrar conexion
conexion.close()