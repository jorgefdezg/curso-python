"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
ACCION            AVENTURA                 DEPORTES
GTA               Assasins                  Fifa 23
COD                CRASH                     Pro 23
PUBG          Prince of Persia             MotoGP 23
"""

tabla = [
    {
        "categoria": "Accion",
        "juegos": ["GTA","COD","PUBG"]
    },
    {
        "categoria": "Aventura",
        "juegos": ["Assassins Creed","Crash","Prince of Persia"]
    },
    {
        "categoria": "Deportes",
        "juegos": ["Fifa 23","Pro 23","Motogp 23"]
    }
]

for categoria in tabla:
    print(f"-----------{categoria['categoria']}-------------")
    for juego in categoria["juegos"]:
        print(juego)