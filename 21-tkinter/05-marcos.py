from tkinter import *

ventana = Tk()

ventana.title("Marcos | Master en PYthon")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250,height=250)
marco_padre.pack(side=BOTTOM,anchor=S,fill=X,expand=YES)

marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="red",
    bd=4,
    relief=SOLID
)
marco.pack(side=LEFT,anchor=SW)

marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="green",
    bd=4,
    relief=SOLID
)
marco.pack(side=RIGHT,anchor=SE)

marco_padre = Frame(ventana, width=250,height=250)
marco_padre.pack(side=TOP,anchor= N,fill=X,expand=YES)


marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="blue",
    bd=4,
    relief=SOLID
)
marco.pack(side=LEFT)

marco.pack(side=LEFT,anchor=SW)

marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="orange",
    bd=4,
    relief=SOLID
)
marco.pack(side=RIGHT)

ventana.mainloop()