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
        # Entrada: obtener los precios de los tres productos
        precio_1 = int(self.txt_importe_1.get())
        precio_2 = int(self.txt_importe_2.get())
        precio_3 = int(self.txt_importe_3.get())

        # Proceso: sumar los tres precios
        total = precio_1 + precio_2 + precio_3 

        # Salida: mostrar la suma
        alert("La suma de los tres productos", ("{0} + {1} + {2} = {3}".format(precio_1, precio_2, precio_3, total)))

    def btn_promedio_on_click(self):
        # B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
        # Entrada: obtener los precios de los tres productos
        precio_1 = int(self.txt_importe_1.get())
        precio_2 = int(self.txt_importe_2.get())
        precio_3 = int(self.txt_importe_3.get())
        lista_precios = [precio_1, precio_2, precio_3]

        # Proceso: calcular el promedio de los tres precios
        lista_precios = [precio_1, precio_2, precio_3]
        promedio = int(sum(lista_precios) / len(lista_precios))

        # Salida: mostrar la suma
        alert("El promedio de los tres productos", ("El promedio = {0}".format(promedio)))


    def btn_total_iva_on_click(self):
        # C	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

        # Entrada: obtener los precios de los tres productos
        precio_1 = int(self.txt_importe_1.get())
        precio_2 = int(self.txt_importe_2.get())
        precio_3 = int(self.txt_importe_3.get())

        # Proceso: sumarlos y agregarle IVA
        lista_precios = [precio_1, precio_2, precio_3]
        iva = int(sum(lista_precios) * 0.21)
        precios_mas_iva = int(sum(lista_precios) * 1.21) 

        # Salida: mostrar el precio final mas IVA
        alert("El precio final + IVA", "${0} + ${1} + ${2} + ${3}(IVA) = ${4}".format(precio_1, precio_2, precio_3, iva, precios_mas_iva))

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()