import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre:
apellido:
---
Ejercicio: for_01
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        for i in range(1, 6):
            alert("titulo", f"{i}")

        # ejemplo análogo con while
        # j = 1
        # while j <= 5:
        #     alert("titulo", f"ahora con while {j}")
        #     j += 1

       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()