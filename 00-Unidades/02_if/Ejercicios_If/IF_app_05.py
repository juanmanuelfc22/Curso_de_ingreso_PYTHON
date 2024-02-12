import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: if_05
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número e informar si la persona "NO ES ADOLESCENTE" utilizando el Dialog Alert.
Enunciado del ejercicio anterior:
edad entre 13 y 17 años ES ADOLESCENTE. Se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Entrada
        # E.1 Obtener la edad de la persona
        # E.2 Convertirlo a número
        edad = self.txt_edad.get()
        edad = int(edad)

        # Proceso
        # P.1 Calcular si es adolescnete 13 y 17 años ES ADOLESCENTE
        if edad >=13 and edad<=17:
            alert("Ejerci num 5 de IF","ES Adolescente")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()