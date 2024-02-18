import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:
apellido:
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
    # Si es invierno: 
    #     Bariloche tiene un aumento del 20% 
    #     Cataratas y Córdoba tienen un descuento del 10%
    #     mar del plata tiene un descuento del 20%
    # si es verano:
    #     bariloche tiene un descuento del 20%
    #     cataratas y cordoba tienen un aumento del 10%
    #     mar del plata tiene un aumento del 20%
    # si es primavera u otoño:
    #     bariloche tiene un aumento del 10%
    #     cataratas tiene un aumento del 10%
    #     mar del plata tiene un aumento del 10%
    #     córdoba tiene precio sin descuento

        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()
        precio = 15000
        # precio_10 = int(precio * 1.1)
        # precio_20 = int(precio * 1.2)
        precio_10 = f"el precio a {destino} en {estacion} es {precio_10}"
        precio_20 = f"el precio a {destino} en {estacion} es {precio_20}"



        match estacion:
            case "Primavera" | "Otoño":
                match destino:
                    case "Cordoba":
                        mensaje = f"el precio a {destino} en {estacion} es {precio}"
                    case _:
                        mensaje = precio_10
                        # mensaje = f"el precio a {destino} en {estacion} es {precio_10}"
            case "Invierno":
                match destino:
                    case "Cataratas" | "Cordoba":
                        mensaje = precio_10
                        # mensaje = f"el precio a {destino} en {estacion} es {precio_10} "
                    case _:
                        mensaje = precio_20
                        # mensaje = f"el precio a {destino} en {estacion} es {precio_20} "
            case "Verano":
                match destino:
                    case "Cataratas" | "Cordoba":
                        mensaje = precio_10
                        # mensaje = f"el precio a {destino} en {estacion} es {precio_10} "
                    case _:
                        mensaje = precio_20
            
        alert("Ejerc 9 de MATCH", mensaje)








   
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()