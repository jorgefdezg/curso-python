from tkinter import *

ventana = Tk()

#ventana.geometry("700x500")

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000", #Hexadecimal
    padx = 50,
    pady = 20,
    font=("Consolas",30)
    )
texto.pack(side=TOP)

texto = Label(ventana, text = "Soy Jorge Fernandez")
texto.config(
    justify=RIGHT,
    height=2,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=TOP,fill=X,expand=YES)

texto = Label(ventana, text = "BASICO1")
texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side= LEFT,fill=X,expand=YES)

texto = Label(ventana, text = "BASICO2")
texto.config(
    height=3,
    bg="blue",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana, text = "BASICO3")
texto.config(
    height=3,
    bg="gray",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)




ventana.mainloop()