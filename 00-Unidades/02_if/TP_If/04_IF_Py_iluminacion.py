import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
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
        cant = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()

        # Proceso y salida
        # En funcion de las reglas de negocio: según la cantidad y la marca de las lamparitas
        # calculo el precio final y luego aplico los descuentos
        precio = 800 * cant

        # Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 
        if cant >= 6:

            # Agregar el descuento adicional del 5% si precio > 4000 
            # ACLARACION! el descuento adicional se aplica SOLAMETENTE
            # si el precio final es mayor a 4000. En la única condición que se
            # aplica el descuento adicional es en la primera condición, 
            # dado que es la única que puede superar los 4000.
            # En las demás condiciones, el precio final no supera los 4000.
            if precio > 4000:
                desc_categoria = int(precio * 0.5)
                tot_parcial = int(precio - desc_categoria)
                desc_adicional = int(tot_parcial * 0.05)
                tot_final = precio - int((desc_categoria + desc_adicional))
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"Total parcial\t ${tot_parcial}\n"
                    f"---\n"
                    f"Desc adicional\t-${desc_adicional}\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)
            else:
                desc_categoria = int(precio * 0.5)
                tot_parcial = int(precio - desc_categoria)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)

        # Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz"
        # se hace un descuento del 40 % y si de otra marca el desc 30%.
        if cant == 5:
            if marca == "ArgentinaLuz":
                desc_categoria = int(precio * 0.4)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)
            else:
                desc_categoria = int(precio * 0.3)
                tot_parcial = int(precio - desc_categoria)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)

        # Si compra 4 lamparitas bajo consumo
        # marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25% 
        # y si es de otra marca el descuento es del 20%.
        if cant == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                desc_categoria = int(precio * 0.25)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)
            else:
                desc_categoria = int(precio * 0.2)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)

        # Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz"
        # el descuento es del 15%,
        # si es “FelipeLamparas” se hace un descuento del 10 % 
        # y si es de otra marca un 5%.
        if cant == 3:
            if marca == "ArgentinaLuz":
                desc_categoria = int(precio * 0.15)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)
            elif marca == "FelipeLamparas":
                desc_categoria = int(precio * 0.1)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)
            else:
                desc_categoria = int(precio * 0.05)
                tot_final = precio - int(desc_categoria)
                
                string_final = (
                    f"Total\t\t ${precio}\n"
                    f"Descuento\t-${desc_categoria}\n"
                    f"---\n"
                    f"TOTAL final\t ${tot_final}"
                )
                alert("TP if",string_final)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()