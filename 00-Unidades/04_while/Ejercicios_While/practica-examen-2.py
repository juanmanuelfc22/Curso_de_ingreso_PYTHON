import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio:  Practica examen 2
---
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        cont_while = 0
        cont_masc = 0
        cont_fem = 0
        cont_nb = 0
        cont_fiebre = 0
        acumulador_nb = 0
        bandera_temp_fem_mas_baja = False
        nombre_temp_fem_mas_baja = ""
        temp_fem_mas_baja = 0


        while cont_while < 5:

            # Ingreso y validaciones iniciales
            nombre = prompt("Nombre", "Ingresar el nombre del paciente")
            while (nombre == None or nombre == ""):
                nombre = prompt("Nombre", "Error: no dejar el campo vacío")

            temp = prompt("Temperatura", "Ingresar la temp del paciente")
            temp = int(temp)
            while (temp == None or temp < 35 or temp > 42):
                temp = prompt("Temperatura", "Error: Ingresar solo temp entre 35 y 42")
                temp = int(temp)

            sexo = prompt("Sexo", "Ingresar el sexo del paciente")
            while (sexo == None or sexo == "" or not(sexo == "m" or sexo == "f" or sexo == "nb")):
                sexo = prompt("Sexo", "Error: solo ingresra 'm', 'f' ó 'nb'")

            edad = prompt("Edad", "Ingresar la edad del paciente")
            edad = int(edad)
            while (edad == None or edad < 1):
                edad = prompt("Edad", "Error: Ingresar edad mayor a 0(cero)")
                edad = int(edad)
                
            detalle_persona = (
                f"Nombre: {nombre}\n"
                f"Temp: {temp}\n"
                f"Sexo: {sexo}\n"
                f"Edad: {edad}\n"
            )

            print (detalle_persona)

            # contabilizar los sexos
            if sexo == "m":
                cont_masc = cont_masc + 1
            elif sexo == "f":
                cont_fem = cont_fem + 1
            else:
                cont_nb = cont_nb + 1
                acumulador_nb = acumulador_nb + edad

            # registrar la temp más baja de sexo fem
            if (sexo == "f" and temp >= 37):
                nombre_temp_fem_mas_baja = nombre
                temp_fem_mas_baja = temp
                bandera_temp_fem_mas_baja = True

            if (bandera_temp_fem_mas_baja == True and temp < temp_fem_mas_baja):
                nombre_temp_fem_mas_baja = nombre
                temp_fem_mas_baja = temp
            
            # contabilizar las personas con fiebre
            if temp >= 37:
                cont_fiebre = cont_fiebre + 1

            cont_while = cont_while + 1 

        # Punto 1. informar el sexo más ingresado
        if (cont_masc > cont_fem and cont_masc > cont_nb):
            print("El sexo más ingresado es el masculino")
        elif (cont_fem > cont_masc and cont_fem > cont_nb):
            print("El sexo más ingresado es el femenino")
        elif (cont_nb > cont_masc and cont_nb > cont_fem):
            print("El sexo más ingresado es el no binario")
        elif (cont_masc == cont_fem and cont_masc > cont_nb):
            print("Los sexos más ingredados fueron los masculinos y fememinos")
        elif (cont_fem == cont_nb and cont_fem > cont_masc):
            print("Los sexos más ingredados fueron los fememinos y no binarios")
        elif (cont_masc == cont_nb and cont_masc > cont_fem):
            print("Los sexos más ingredados fueron los binarios y no binarios")
        else:
            print("Error de cómputo")

        # Punto 2. informar el porcentaje de personas con o sin fiebre
        personas_con_fiebre = (cont_fiebre / 5) * 100
        personas_con_fiebre = round(personas_con_fiebre, 2)
        personas_sin_fiebre = 100 - personas_con_fiebre
        print(f"El % de personas con fiebre es {personas_con_fiebre}%")
        print(f"El % de personas sin fiebre es {personas_sin_fiebre}%")

        # Punto 3. Informar la cant de personas de sexo masculino
        if cont_masc > 0:
            print(f"La cant de personas de sexo masculino es {cont_masc}")
        else:
            print("No se registraron personas de sexo masculino")

        # Punto 4. Informar la edad promedio de personas de sexo nb
        if cont_nb > 0:
            promedio_nb = acumulador_nb / cont_nb
            promedio_nb = round(promedio_nb)
            print(f"El promedio de edad de las personsa nb es {promedio_nb}")
        else:
            print("No se registraron personas de sexo nb calcular su promedio")

        # Punto 5. El nombre de la persona se sexo fem con la temp más baja
        if (sexo == "f" and temp >= 37):
            bandera_temp_fem_mas_baja = True
            nombre_temp_fem_mas_baja = nombre
            temp_fem_mas_baja = temp

        if (bandera_temp_fem_mas_baja == True and temp < temp_fem_mas_baja):
            nombre_temp_fem_mas_baja = nombre
            temp_fem_mas_baja = temp

        if bandera_temp_fem_mas_baja == True:
            print(f"El nombre de la mujer con temp más baja es {nombre_temp_fem_mas_baja}")
        else:
            print("No se registraron mujeres para indicar su temp más baja")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
