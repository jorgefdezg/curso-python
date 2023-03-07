"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, añadir, informacion, salir)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opcion de salir
"""
from tkinter import *
from tkinter import ttk

#Definir ventana
ventana = Tk()
#ventana.geometry("600x500")
ventana.minsize(500,500)
ventana.title("Proyecto Tkinter")
ventana.resizable(0,0)


#Pantallas
def home():
    #Montar pantallas
    home_label.config(
        fg="white",
        bg = "black",
        font = ("Arial",30),
        padx=260,
        pady=20
    )
    home_label.grid(row=0,column=0)

    productos_box.grid(row=2)
    #Listar productos
    """
    for product in productos:
        if len(product) == 3:
            product.append("anadido")
            Label(productos_box,text=product[0]).grid()
            Label(productos_box,text=product[1]).grid()
            Label(productos_box,text=product[2]).grid()
            Label(productos_box,text="----------------------------").grid()
    """
    for product in productos:
        if len(product) == 3:
            product.append("anadido")
            productos_box.insert("",0,text=product[0], values=(product[1]))
    #Ocultar otras pantallas
    data_label.grid_remove()
    anadir_label.grid_remove()
    info_label.grid_remove()
    add_frame.grid_remove()

    return True

def anadir():
    anadir_label.config(
        fg="white",
        bg = "black",
        font = ("Arial",30),
        padx=160,
        pady=20
    )
    anadir_label.grid(row=0,column=0,columnspan=16)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name.grid(row=1,column=0,padx=5,pady=5,sticky=W)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    price_name.grid(row=2,column=0,padx=5,pady=5,sticky=W)
    price_name_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    description_name.grid(row=3,column=0,padx=5,pady=5,sticky=NW)
    description_name_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    description_name_entry.config(
        width=30,
        height=5,
        font=("Consolas",12),
        padx=15,
        pady=15
    )

    Label(add_frame,text="").grid(row=4)

    boton.grid(row=5,column=1, sticky=NW)
    boton.config(
        bg="black",
        fg="white"
    )



    #Ocultar otras pantallas
    data_label.grid_remove()
    home_label.grid_remove()
    info_label.grid_remove()
    productos_box.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg = "black",
        font = ("Arial",30),
        padx=200,
        pady=20
    )
    info_label.grid(row=0,column=0)

    data_label.grid(row=1,column=0)

    #Ocultar otras pantallas
    home_label.grid_remove()
    anadir_label.grid_remove()
    add_frame.grid_remove()
    productos_box.grid_remove()
    return True

def anadir_producto():
    productos.append([
        name_data.get(),
        price_data.get(),
        description_name_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    description_name_entry.delete("1.0", END)
    
    home()


#Variables formulario
productos = []
name_data = StringVar()
price_data = IntVar()

#Definir campos de pantallas (home)
home_label = Label(ventana, text="Inicio")
#productos_box = Frame(ventana, width=250)

#Crear tabla
Label(ventana).grid(row=1)
productos_box = ttk.Treeview(height=12,columns=2)
productos_box.grid(row=1,column=0,columnspan=2)
productos_box.heading("#0", text="Producto", anchor=W)
productos_box.heading("#1", text="Precio", anchor=W)

#Definir campos de pantallas (añadir)
anadir_label = Label(ventana, text="Añadir producto")

#Crear campos del formulario
add_frame = Frame(ventana)
add_name = Label(add_frame, text="Nombre del producto")
add_name_entry = Entry(add_frame, textvariable=name_data)

price_name = Label(add_frame, text="Precio del producto")
price_name_entry = Entry(add_frame, textvariable=price_data)

description_name = Label(add_frame, text="Descripcion del producto")
description_name_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command=anadir_producto)

#Definir campos de pantallas (informacion)
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Jorge Fernandez - 2023")

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio",command=home)
menu_superior.add_command(label="Añadir",command=anadir)
menu_superior.add_command(label="Informacion",command=info)
menu_superior.add_command(label="Salir", command= ventana.quit)


#Cargar menu
ventana.config(menu=menu_superior)

home()
#Cargar ventana
ventana.mainloop()