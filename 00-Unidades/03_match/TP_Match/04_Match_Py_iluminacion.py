import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
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
    # Todas las lámparas están  al mismo precio de $800 pesos final.
		# A. Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
        #
		# B. Si compra 5  lamparitas bajo consumo
        # marca "ArgentinaLuz" se hace un descuento del 40 %
        # si es de otra marca el descuento es del 30%.
        #
		# C. Si compra 4  lamparitas bajo consumo
        # marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 %
        # y si es de otra marca el descuento es del 20%.
        #
		# D. Si compra 3  lamparitas bajo consumo
        # marca "ArgentinaLuz"  el descuento es del 15%,
        # si es  “FelipeLamparas” se hace un descuento del 10 %
        # y si es de otra marca un 5%.
        # 
		# E. Si el importe final con descuento suma más de $4000
        # se obtien un descuento adicional de 5%.
        cant_lamp = self.combobox_cantidad.get()
        cant_lamp = int(cant_lamp)

        marca = self.combobox_marca.get()

        fc_inicial = cant_lamp * 800
        descuento = 0

        match cant_lamp:
            case cant_lamp if cant_lamp >= 6:
                descuento = 0.5
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 0.4
                    case _:
                        descuento = 0.3
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = 0.25
                    case _:
                        descuento = 0.2
            case 3:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 0.15
                    case "FelipeLamparas":
                        descuento = 0.1
                    case _:
                        descuento = 0.05
            case _:
                descuento = 0

        monto_desc = int(fc_inicial * descuento)
        fc_total = fc_inicial - monto_desc
        fc_final = fc_total


        match fc_total:
            case fc_total if fc_total > 4000:
                desc_adicional = 0.05
                monto_desc_adic = fc_total * desc_adicional
                fc_final = fc_total - monto_desc_adic
            case _:
                monto_desc_adic = 0


        informe_final = (
            f"Compra de {cant_lamp} u. {marca}\n\n"
            f"Total\t\t ${fc_inicial}\n"
            f"Descuento {int((descuento * 100))}%\t-${monto_desc}\n"
            f"Total parcial\t ${fc_total}\n"
            f"---\n"
            f"Desc +5% si parcial supera $4000\n"
            f"Desc adic.\t-${monto_desc_adic}\n"
            f"TOTAL final\t ${fc_final}"
        )

        alert("TP MATCH", informe_final)


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()