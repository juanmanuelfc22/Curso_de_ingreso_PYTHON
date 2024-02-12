import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: if_07
---
Enunciado:
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos
naturalizados desde los dieciocho (18) años están habilitados a votar. 
Al presionar el botón 'Mostrar', se deberá informar (utilizando el Dialog Alert) 
si es o no posible que la persona concurra a votar en base a la información 
suministrada.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["NATIVO", "NATURALIZADO"])
        self.combobox_tipo.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Eligibilidad de Voto", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Entrada
        # E1. Obtener la edad de la persona
        # E2. Convertir la edad de la persona a número
        # E3. Obtener el estado de residencia de la persona
        edad = self.txt_edad.get()
        edad = int(edad)
        estado = self.combobox_tipo.get()
        print(edad ,estado)

        # Proceso y salida
        # P1. verificar la edad
        # P2. verificar la combo de edad y estado naturalizado
        # P3. en fn de las diferentes combos informar salida si puede o no

        # Cadenas para el resultado
        titulo = "Ejercicio num 7 IF"
        votar_si = "PUEDE VOTAR."
        votar_no = "NO PUEDE VOTAR."
        menor_nac = "Siendo Arg. nativo debe tener mínimo 16 años para votar"
        menor_nat = "Siendo naturalizado debe tener mínimo 18 años para votar"

        if edad < 16:
            if estado == "NATIVO":
                alert(titulo, "{0} {1}".format(votar_no, menor_nac))
            else:
            # if estado == "NATURALIZADO":
                alert(titulo, "{0} {1}".format(votar_no, menor_nat))
        elif edad >= 16 and edad <18:
            if estado == "NATIVO":
                alert(titulo, votar_si)
            else:
                alert(titulo, "{0} {1}".format(votar_no, menor_nat))
        else:
            alert(titulo, votar_si)




        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()