import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio:  Practica examen
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        cont_while = 0

        cont_personas = 0
        cont_masc = 0
        cont_fem = 0
        cont_nb = 0
        cont_fiebre = 0
        cont_menor = 0
        cont_menor_y_fiebre = 0
        acumu_fiebre = 0
        registro_temp_mas_baja_fem = False
        mombre_temp_mas_baja_fem = ""
        temp_mas_baja_fem = 0

        while cont_while <= 5:

            # Prompts y validaciones iniciales
            nombre = prompt("Nombre", "Ingresar nombre")
            while (nombre == None or nombre == ""):
                nombre = prompt("Nombre", "Ingresar un nombre válido")
            
            temp = prompt("Temperatura", "Ingresar temperatura")
            temp = int(temp)
            while (temp == None or temp < 35 or temp > 42):
                msg_temp_error = "Para la temp ingresar un num entre 35 y 42"
                temp = prompt("Temperatura",msg_temp_error)

            sexo = prompt("Sexo", "Ingresar sexo: 'm', 'f' ó 'nb'")
            while (sexo == None or sexo == "" or not(sexo == "m" or sexo == "f" or sexo == "nb")):
                sexo = prompt("Sexo", "Ingresar solo 'm', 'f' ó 'nb'")

            edad = prompt("Edad", "Ingresar edad")
            edad = int(edad)
            while (edad == None or edad <= 0):
                edad = prompt("Edad", "Ingresar edad mayor a 0(cero)")
                edad = int(edad)

            datos_persona = (
                f"Nombre: {nombre}\n"
                f"Temp: {temp}\n"
                f"Sexo: {sexo}\n"
                f"Edad: {edad}\n"
            )

            # Imprimir los datos de las peronas
            print(datos_persona)

            # Empezar la contabilización del bucle y recopilación de datos
            cont_personas = cont_personas + 1

            # contador de los sexos para luego informar la cant de personas
            # de sexo fem y mas
            if sexo == "m":
                cont_masc = cont_masc + 1
            elif sexo == "f":
                cont_fem = cont_fem + 1
            else:
                cont_nb = cont_nb + 1

            # contador de personas con fiebre y acumulador de la "cant"
            # de fiebre para luego sacar: % de personas con y sin fiebre como
            #  así también la temp promedio de las personas menores de edad
            if temp >= 37:
                cont_fiebre = cont_fiebre + 1
                acumu_fiebre = acumu_fiebre + temp

            # contador de las personas menores de edad
            if edad < 18:
                cont_menor = cont_menor + 1

            # cont de personas menores que tieneen fiebre
            if edad < 18 and temp >= 37:
                cont_menor_y_fiebre = cont_menor_y_fiebre + 1

            # Si la persona es de sexo f y registra fiebre, guardar
            # su nombre y su temp registrada de fiebre
            # también cambiar el valor de la bandera si existe tal perosona
            # (mujer con fiebre)
            if (sexo == "f" and temp >= 37):
                registro_temp_mas_baja_fem = True
                mombre_temp_mas_baja_fem = nombre
                temp_mas_baja_fem = temp

            # si bandera de la mujer de arriba existe, y si su temp es más
            # baja de la registrada, guardar los datos otra vez: nombre y temp
            if (registro_temp_mas_baja_fem == True and temp < temp_mas_baja_fem):
                mombre_temp_mas_baja_fem = nombre
                temp_mas_baja_fem = temp

            # Darle otra vuelta de tuerca al while
            cont_while = cont_while + 1


                

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()