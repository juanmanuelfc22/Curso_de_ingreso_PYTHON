import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: if_03bis
---
Enunciado:
A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir mas de 1.80 metros
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        # La consigna pide que se ingrese la altura del basquetbolista
        # pero el label dice edad. Cambio el label por altura
        self.txt_altura = customtkinter.CTkEntry(master=self)
        self.txt_altura.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
    # A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no.
    # Para serlo el mismo deberá medir mas de 1.80 metros

    # Entrada.
    # E.1 Obtener la altura del basquetbolista.
    # E.2 Convertir la altura a float.
        altura = self.txt_altura.get()
        altura = float(altura)

    # Proceso y Salida
    # P.1 Verificar si la altura es mayor a 1.80
    # S.1 Si cumple o no la condición mostrar el resultado
        if altura > 1.80:
            alert("Resultado", "Es Pivot")

        if altura <= 1.80:
            alert("Resultado", "No es Pivot")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()