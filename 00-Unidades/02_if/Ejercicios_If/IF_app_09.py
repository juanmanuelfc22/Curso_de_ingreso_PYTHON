import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Juan Manuel
apellido: Fernández Casenve
---
Ejercicio: if_09
---
Al presionar el botón  'Calcular', se deberá mostrar (utilizando el Dialog alert) un número
aleatorio entre el 1 y el 10 inclusive
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Entrada y Proceso
        # E1 y P1 generar el num aleatorio entre 1 y 10 inclusive
        numero_aleatorio = random.randint(1, 10)

        # Salida
        # S1. Mostrar por alert el numero generado
        titulo = "Ejercicio 9 de IF"
        alert(titulo, "Un num aleatorio entre 1 y 10: {0}". format(numero_aleatorio))

        

    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()