import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Juan Manuel
apellido: Fernádez Casenave
---
Ejercicio: if_10
---
Enunciado:
Al presionar el botón 'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Enunciado
        # Al presionar el botón 'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive,
        # para luego mostrar un mensaje según el valor:
        # 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
        # 4 y 5           ---> Aprobado, la nota es ...
        # 1, 2 y 3        ---> Desaprobado, la nota es ...

        # Entrada y Proceso
        # E1 y P1 generar el num aleatorio entre 1 y 10 inclusive
        numero_aleatorio = random.randint(1, 10)

        # Salida
        # S1. Mostrar por alert el numero generado con sus respectivas leyendad
        titulo = "Ejercicio 10 de IF"
        desaprobado = "Desaprobado, la nota es "
        aprobado = "Aprobado, la nota es "
        promomocion = "Promoción directa, la nota es "

        # if (numero_aleatorio <= 3):
        #     alert(titulo, "{0} {1}".format(desaprobado, numero_aleatorio))
        # elif (numero_aleatorio > 3 and numero_aleatorio <= 5):
        #     alert(titulo, "{0} {1}".format(aprobado, numero_aleatorio))
        # else:
        #     alert(titulo, "{0} {1}".format(promomocion, numero_aleatorio))

        if (numero_aleatorio > 3):
            if (numero_aleatorio >5):
               alert(titulo, "{0} {1}".format(promomocion, numero_aleatorio))
            else:
                alert(titulo, "{0} {1}".format(aprobado, numero_aleatorio))
        else:
            alert(titulo, "{0} {1}".format(desaprobado, numero_aleatorio))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()