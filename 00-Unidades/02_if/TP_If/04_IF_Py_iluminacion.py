import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están al mismo precio de $800 pesos final.

		A.	Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 

		B.	Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz"
        => se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.

		C. Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas”
        => se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.

		D.	Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz"
        => el descuento es del 15%,
        => si es “FelipeLamparas” se hace un descuento del 10 % 
        => y si es de otra marca un 5%.

		E.	Si el importe final con descuento suma más de $4000 se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):

        # Entrada
        # E1. Obtener la cantidad de lamparitas
        # E2. Obtener la marca de las lamparitas
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()

        # Proceso y salida
        # En funcion de las reglas de negocio: según la cantidad y la marca de las lamparitas
        # calculo el precio final y luego aplico los descuentos
        precio = 800 * cantidad

        # Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 
        if cantidad >= 6:
            desc = int(precio * 0.5)
            desc_str = "Descuento -$" + str(desc) + "\n"
            total = int(precio - desc)
            tot_str = "Total $" + str(total) + "\n"

            if total > 4000:
                desc_adicional = int(total * .05)
                desc_adic_str = "Descuento adic -$" + str(desc_adicional) + "\n"
                total_final = precio - desc_adicional
                total_final_str = "TOTAL FINAL $" + str(total_final)
                alert("TP if", "${0}{1}{2}{3}{4}".format(total, desc_str, tot_str, desc_adic_str, total_final_str))

            # alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
        # Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz"
        # se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                descuento = int(precio * 0.4)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
            else:
                descuento = int(precio * 0.3)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
        # Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas”
        # se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                descuento = int(precio * 0.25)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
            else:
                descuento = int(precio * 0.2)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
        # Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz"
        # el descuento es del 15%, si es “FelipeLamparas” se hace un descuento del 10 % 
        # y si es de otra marca un 5%.
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                descuento = int(precio * 0.15)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
            elif marca == "FelipeLamparas":
                descuento = int(precio * 0.1)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
            else:
                descuento = int(precio * 0.05)
                total = int(precio - descuento)
                alert("TP if", "Precio ${0}\n- Descuento ${1}\nTotal ${2}".format(precio, descuento, total))
        else:
            alert("TP if", "No se puedo calcular por haber comprado menos de 3 lamparitas")





        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
