import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Manuel
apellido: Fernandez Casenave
---
Ejercicio: Match_07
---
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        
        destino = self.combobox_destino.get()

        match destino:
            case "Bariloche":
                mensaje = "Bariloche se encuentra en el oeste"
            case "Mar del plata":
                mensaje = "Bariloche se encuentra en el este"
            case "Cataratas":
                mensaje = "Bariloche se encuentra en el norte"
            case "Ushuaia":
                mensaje = "Bariloche se encuentra en el sur"

        alert("Ejer 7 MATCH", mensaje)

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()