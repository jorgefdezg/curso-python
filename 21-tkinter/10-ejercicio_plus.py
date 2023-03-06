    
from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self,alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def convertirFloat(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos!")

        return result


    def sumar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) + self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) - self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()


    def multiplicar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) * self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) / self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()


    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operacion es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("Ejercicio")
ventana.geometry("400x400")


calculadora = Calculadora(messagebox)

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
Entry(marco, textvariable=calculadora.numero1,justify=CENTER).pack(anchor=W)

Label(marco,text="Escriba el segundo numero: ",justify=CENTER).pack(anchor=W)
Entry(marco, textvariable=calculadora.numero2,justify=CENTER).pack(anchor=W)


Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X,expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X,expand=YES)




ventana.mainloop()