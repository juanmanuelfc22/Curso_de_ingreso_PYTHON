import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener el valor contenido en la caja de texto (txt_importe), 
transformarlo a número y mostrar el importe actualizado con un descuento del 20% utilizando el Dialog Alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # Entrada: obtener el valor del importe y convertirlo a int
        importe = int(self.txt_importe.get())
        
        # Proceso: descontarle un 20% al importe
        descuento = int(importe * 0.20)
        importe_final = int(importe - descuento)


        # Salida: mostrar la info en un alert
        alert("El importe menos 20%",
              "Importe original\t${0}\n- 20% \t\t- ${1}\n\t\t---\nImporte final\t${2}".format(importe, descuento, importe_final))

        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
