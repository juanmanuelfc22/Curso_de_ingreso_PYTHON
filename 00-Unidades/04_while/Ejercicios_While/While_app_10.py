import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        suma_neg = 0
        suma_pos = 0
        cant_pos = 0
        cant_neg = 0
        cant_ceros = 0

        while True:

            numero = prompt("Titulo", "Ingresar un numero")

            if numero is None:
                break
            else:

                numero = int(numero)

                if numero > 0:
                    cant_pos = cant_pos + 1
                    suma_pos = suma_pos + numero
                elif numero < 0:
                    cant_neg = cant_neg + 1
                    suma_neg = suma_neg + numero
                else:
                    cant_ceros = cant_ceros + 1


        dif_pos_neg = cant_pos - cant_neg

        resultado = (
            f"Cant de positivos:\t\t{cant_pos}\n"
            f"Suma de positivos:\t{suma_pos}\n"
            f"Cant de negativos:\t{cant_neg}\n"
            f"Suma de negativos:\t{suma_neg}\n"
            f"Cant de ceros:\t\t{cant_ceros}\n"
            f"Dif de pos y neg:\t\t{dif_pos_neg}\n"
        )

        alert("Titulo",resultado)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
