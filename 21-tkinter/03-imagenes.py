from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")



Label(ventana,text="Hola, soy Jorge").pack()

imagen = Image.open("./imagenes/imagen.jpg")
render = ImageTk.PhotoImage(imagen)

Label(ventana,image=render).pack()

ventana.mainloop()