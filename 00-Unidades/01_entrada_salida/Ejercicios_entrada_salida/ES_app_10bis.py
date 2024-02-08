import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: entrada_salida_10bis
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(
            master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto
        # (txt_importe y txt_descuento), 
        # transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.

        # Entrada: obtener los valores de txt_importe y txt_descuento
        importe = int(self.txt_importe.get())
        descuento = int(self.txt_descuento.get())

        # Proceso: aplicarle el descuento al importe
        importe_descontado = int(importe * ((descuento/100)))
        importe_final = importe - importe_descontado

        # Salida: informar por alert el importe final con el desc aplicado
        alert("El importe con el descuento aplicado","${0} - {1}% = ${2}". format(importe, descuento, importe_final))




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
