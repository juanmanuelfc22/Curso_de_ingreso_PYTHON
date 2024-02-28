import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Simulacro de parcial 2024-02-28
---

Enunciado:
Se desea desarrollar un programa para 10 videojuegos que permita al usuario ingresar 
1. nombre
2. año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015)
3. si es online u offline
4. costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        juego_mas_barato = 0
        juego_mas_caro = 0
        juego_mas_bararo_pre_2015 = 0
        juego_mas_caro_pre_2015 = 0
        acumulador_costo_online = 0
        cont_offline = 0
        cont_online = 0
        cont_pre_2000 = 0
        cont_2000_a_2015 = 0
        cont_post_2015 = 0
        promedio_juegos_online = 0

        for i in range (1, 11):

            nombre = prompt("Nombre", "Ingresar el nombre del videojuego")
            while (nombre == None or nombre == ""):
                nombre = prompt("Nombre", "Error: Ingresar el nombre del videojuego")

            year = prompt("Año", "Ingrese el año que se emitió el videojuego")
            year = int(year)
            while (year == None or year <1980 or year >2024):
                year = prompt("Año", "Error: Ingrese el año desde 1980 hasta 2024")
                year = int(year)

            estado = prompt("Estdo", "Ingresar si el juego es 'Online' o 'Offline'")
            while (estado == None or estado == ""):
                estado = prompt("Estdo", "Ingresar solamente 'Online' ó 'Offline'")

            costo = prompt("Costo", "Ingresar el costo del juego")
            costo = int(costo)
            while (costo == None or costo < 500 and costo > 10000):
                costo = prompt("Costo", "Error: Ingresar un valor entre 500 y 10000")
                costo = int(costo)

            # Encontrar el videojuego más caro y el más barato ingresado 
            if i == 1:
                juego_mas_barato = costo
                juego_mas_caro = costo
            else:
                if costo < juego_mas_barato:
                    juego_mas_barato = costo
                if costo > juego_mas_caro:
                    juego_mas_caro = costo

            # Calcular el promedio de los costos de los videojuegos
            # pero solo para aquellos que son online.
            if estado == "Online":
                acumulador_costo_online = acumulador_costo_online + costo

            # Encontrar los videojuegos con el costo máximo y mínimo
            # de aquellos emitidos antes de 2015
            if i == 1 and year < 2015:
                juego_mas_bararo_pre_2015 = costo
                juego_mas_caro_pre_2015 = costo

            if year < 2015 and costo > juego_mas_caro_pre_2015:
                juego_mas_caro_pre_2015 = costo
            if year < 2015 and costo < juego_mas_bararo_pre_2015:
                juego_mas_bararo_pre_2015 = costo

            # Calcular el porcentaje de videojuegos offline en relación
            # al total de videojuegos ingresados.
            if estado == "Online":
                cont_online = cont_online + 1
            else:
                cont_offline = cont_offline + 1

            # Informar a que rango de año emitido pertenecen
            # la mayor parte de los videojuegos vendidos.
            if year < 2000:
                cont_pre_2000 = cont_pre_2000 + 1
            else:
                if year >= 2000 and year <= 2015:
                    cont_2000_a_2015 = cont_2000_a_2015 + 1
                else:
                    cont_post_2015 = cont_post_2015 + 1

        # Informe el videojuego más caro y el más barato ingresado.
        # Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.

        promedio_juegos_online = acumulador_costo_online / cont_online
        resultado_promedio_juegos_online = ""
        if (cont_online > 0):
            resultado_promedio_juegos_online = promedio_juegos_online
        else:
            resultado_promedio_juegos_online = "No se encontraron juegos online para calcular promedio"
            
        # Encontrar los videojuegos con el costo máximo y mínimo de
        # aquellos emitidos antes de 2015.

        
        # Calcular el porcentaje de videojuegos offline en
        # relación al total de videojuegos ingresados.
        resultado_porcentaje_offline = ""
        if (cont_offline > 0):
            porcentaje_offline = (cont_offline / 10) * 100
            porcentaje_offline = round(porcentaje_offline)
        else:
            porcentaje_offline = "No se registraron juegos offline"

        # Informar a que rango de año emitido pertenecen
        #  la mayor parte de los videojuegos vendidos.
        mayoria_anio_emitido = ""
        if cont_pre_2000 > cont_2000_a_2015 and cont_pre_2000 > cont_post_2015:
            mayoria_anio_emitido = "antes del 2000"
        elif cont_2000_a_2015 > cont_pre_2000 and cont_2000_a_2015 > cont_post_2015:
            mayoria_anio_emitido = "entre 2001 y 2015"
        else:
            mayoria_anio_emitido = "post 2015"


        resultado = (
            f"El juego más barato cuesta: ${juego_mas_barato}\n"
            f"El juego más caro cuesta: ${juego_mas_caro}\n"
            f"El promedio de los juegos online: ${resultado_promedio_juegos_online}\n"
            f"El juego mas caro pre 2015 cuesta: ${juego_mas_caro_pre_2015}\n"
            f"El juego mas barato pre 2015 cuesta: ${juego_mas_bararo_pre_2015}\n"
            f"El porcentaje % de los juegos offline es: {porcentaje_offline}\n"
            f"La mayoria de los juegos se emitieron {mayoria_anio_emitido}"
        )

        alert("Los resultados", resultado)



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
