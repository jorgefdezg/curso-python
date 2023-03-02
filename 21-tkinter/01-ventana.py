"""
Tkinter.
Modulo para crear interfaces graficas de usuario.
"""

from tkinter import *
import os
from pathlib import Path


class Programa:

    def __init__(self):
        self.title = "Master en Python con Victor Robles"
        self.icon = "@imagenes/icon.xbm"
        self.icon_alt = "./21-tkinter/imagenes/icon.ico"
        self.size = "770x470"
        self.resizable = False


    def cargar(self):
        #Crear una ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.title)

        #Comprobar si existe un archivo
        ruta_icono = os.path.abspath("./imagenes/icon.ico")

        #Icono de la ventana
        Wpath = Path('icon.ico').absolute()
        Upath = Path('icon.xmb').absolute()
        if "nt" == os.name:
            if not os.path.isfile(ruta_icono):
                ruta_icono=os.path.abspath(self.icon_alt)
            ventana.wm_iconbitmap(ruta_icono)
            texto = Label(ventana, text=Wpath)
            texto.pack()
        else:
            ventana.wm_iconbitmap(bitmap=self.icon)
            texto = Label(ventana, text=Upath)
            texto.pack()

        #Cambiar tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)


    def addTexto(self,dato):
        texto = Label(self.ventana,text=dato)
        texto.pack()

    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

#Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola, soy un texto")
programa.mostrar()