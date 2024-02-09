import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: if_03
---
Enunciado:
Al presionar el botón 'Calcular',
 se deberá obtener el contenido de la caja de texto txtEdad, 
 transformarlo en número y calcular si es o no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso contrario “MENOR” en ambos casos utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Entrada
        # E.1 Obtener el valor del texto de txt_edad
        # E.1 Convertirlo a número
        edad = self.txt_edad.get()
        edad = int(edad)

        # Proceso
        # P.1 Preparar el mensaje
        # P.2 evaluar si es mayor de edad o no
        # P.3 actualizar al mensaje en funcion de P.2
        mensaje = ""
        if edad <18:
            mensaje = "MENOR"
        
        if edad >=18:
            mensaje = "MAYOR"

        # Salida
        # S.1 mostar por alert el resultado del proceso
        alert("Ejercicios IF num 3", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()