"""
Calculadora:
-Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio")
ventana.geometry("400x400")

def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos!")

    return result


def sumar():
    try:
        resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    mostrarResultado()


def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")



numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana,width=360,height=200)
marco.config(
    bd = 5,
    padx= 15,
    pady=15,
    relief=SOLID
)
marco.pack(side = TOP, anchor= CENTER)
marco.pack_propagate(False)


Label(marco,text="Escriba el primer numero: ").pack(anchor=W)
Entry(marco, textvariable=numero1,justify=CENTER).pack(anchor=W)

Label(marco,text="Escriba el segundo numero: ",justify=CENTER).pack(anchor=W)
Entry(marco, textvariable=numero2,justify=CENTER).pack(anchor=W)


Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X,expand=YES)




ventana.mainloop()