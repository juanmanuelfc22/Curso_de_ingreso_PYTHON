import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # self      el objeto que se está creando
        # .title    el (atributo?) del objeto? es parte del objeto que se está creando
        # ("UTN FRA 2024")  el argumento que se le está pasando al title
        # el título de la ventana que aparece cuando se ejecuta "play" en el editor de código
        self.title("UTN FRA 2024")

        # .label1
        # la "etiqueta" que aparece en la ventana, como si fuese el <label> de HTML?
        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre y Apellido:")

        # el tamaño del labal
        # padx = padding horizontal a izquierda y derecha de la etiqueta
        # pady = padding vertical arriba y abajo de la etiqueta
        # self.label1.grid(row=0, column=0, padx=190, pady=230)
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        # txt_nombre = el texto que se ingresa en la caja de texto 
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Obtengo el texto de self.txt_nombre
        texto_ingresado = self.txt_nombre.get()
        # calculo la cantidad de caracteres del texto ingresado
        caracteres = len(texto_ingresado)
        # los borro
        self.txt_nombre.delete(0, caracteres)
        # los ingreso nuevament
        self.txt_nombre.insert(0, texto_ingresado)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()