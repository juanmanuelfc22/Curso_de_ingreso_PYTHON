import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_04
---
Enunciado:
Al presionar el botón 'Mostrar' pedir 10 valores por prompt o hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Al presionar el botón 'Mostrar' pedir 10 valores por prompt  
        # o hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').

        for i in range(1, 11):
            valor = prompt("titulo", "Ingresar un numero")
            if valor == None or valor == "9":
                break
            else:
                alert("titulo", f"El valor ingresado es: {valor}")





        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()