from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()
ventana.config(
    bd = 70
)

def sacarAlerta():
    Messagebox.showerror("Alerta", "Hola soy Victor Robles")

Button(ventana, text="Mostrar alerta!!", command=sacarAlerta).pack()


def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "¿Continuar ejecutando la aplicacion?")
    
    if resultado != "yes":
        Messagebox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Jorge Fernandez")).pack()


ventana.mainloop()