import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        # A. Ingresar tres precios de productos y mostrar la suma de los mismos.
        prec1 = int(self.txt_importe_1.get())
        prec2 = int(self.txt_importe_2.get())
        prec3 = int(self.txt_importe_3.get())

        suma = prec1 + prec2 + prec3 

        titulo = "TP 1 Entrada/Salida"

        resultado = f"${prec1} + ${prec2} + ${prec3} = ${suma}"

        alert(titulo, resultado)


    def btn_promedio_on_click(self):
        # B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
        prec1 = int(self.txt_importe_1.get())
        prec2 = int(self.txt_importe_2.get())
        prec3 = int(self.txt_importe_3.get())

        suma = prec1 + prec2 + prec3 
        promedio = int(suma / 3)

        titulo = "TP 1 Entrada/Salida"
        resultado = f"El promedio de {prec1}, {prec2} y {prec3} es {promedio}"

        alert(titulo, resultado)


    def btn_total_iva_on_click(self):
        # C	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

        prec1 = int(self.txt_importe_1.get())
        prec2 = int(self.txt_importe_2.get())
        prec3 = int(self.txt_importe_3.get())

        suma = prec1 + prec2 + prec3 
        iva = int(suma * 0.21)
        prec_con_iva = int(suma + iva)


        titulo = "TP 1 Entrada/Salida"
        resultado = (
            f"\t${prec1}\n"
            f"+\t${prec2}\n"
            f"+\t${prec3}\n"
            f"\t------\n"
            f"sub tot\t${suma}\n"
            f"+ iva\t${iva}\n"
            f"\t------\n"
            f"TOTAL\t${prec_con_iva}\n"
        )

        alert(titulo, resultado)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()