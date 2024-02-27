import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        cont_masc = 0
        acumu_edad_masc = 0
        promedio_edad_masc = 0
        cont_fem = 0
        acumu_edad_fem = 0
        promedio_edad_fem = 0
        cont_nb = 0
        acumu_edad_nb = 0
        promedio_edad_nb = 0
        cont_js = 0
        cont_asp = 0
        cont_python = 0
        cont_post_complejo = 0
        nombre_jr = ""
        edad_jr = 130 
        bandera_jr = False

        for i in range(1, 5):

            nombre = prompt("Nombre", "Ingresar el nombre")
            while (nombre == None or nombre == ""):
                nombre = prompt("Nombre", "Ingresar el nombre")
                nombre = nombre.upper()

            edad = prompt("Edad", "Ingresar la edad")
            edad = int(edad)
            while (edad == None or edad <= 0):
                edad = prompt("Edad", "Error: ingresar la edad mayor a cero(0)")
                edad = int(edad)

            sexo = prompt("Sexo", "Ingresar el sexo")
            while (sexo == None or sexo == "" or not(sexo == "M" or sexo == "F" or sexo == "NB")):
                sexo = prompt("Sexo", "Error: Ingresar solo 'M', 'F', ó 'NB'")
                sexo = sexo.upper()

            tecno = prompt("Tecnologia", "Ingresar la tecnologia")
            while (tecno == None or tecno == "" or not(tecno == "ASP.NET" or tecno == "JS" or tecno == "PYTHON")):
                tecno = prompt("Tecnologia", "Error: ingresar solo 'ASP.NET', 'JS' ó 'PYTHON'")
                tecno = tecno.upper()
            
            puesto = prompt("Puesto", "Ingresar el puesto")
            while (puesto == None or puesto == "" or not(puesto == "JR" or puesto == "SSR" or puesto == "SR")):
                puesto = prompt("Tecnologia", "Error: ingresar solo 'JR', 'SSR' ó 'SR'")
                puesto = puesto.upper()

            persona = (
                f"Candidato {i}\n"
                f"Nombre: {nombre}\n"
                f"Edad: {edad}\n"
                f"Genero: {sexo}\n"
                f"Tencología: {tecno}\n"
                f"Puesto: {puesto}\n"
            )

            print(persona)

            # Contabilizar las personas por género
            if sexo == "M":
                cont_masc = cont_masc + 1
                acumu_edad_masc = acumu_edad_masc + edad
            elif sexo == "F":
                cont_fem = cont_fem + 1
                acumu_edad_fem = acumu_edad_fem + edad
            else:
                cont_nb = cont_nb + 1
                acumu_edad_nb = acumu_edad_nb + edad

            # Contabilizar las tecnlodgias
            match (tecno):
                case "ASP.NET":
                    cont_asp = cont_asp + 1
                case "JS":
                    cont_js = cont_js + 1
                case "PYTHON":
                    cont_python = cont_python + 1

            # Cantidad de postulantes de genero no binario (NB)
            # que programan en ASP.NET o JS cuya edad este entre 25 y 40,
            # que se hayan postulado para un puesto Ssr.
            if (sexo == "NB" and (tecno == "ASP.NET" or tecno == "JS") and (edad >= 25 and edad <= 42) and puesto == "SSR"):
                cont_post_complejo = cont_post_complejo + 1

            # Nombre del postulante Jr con menor edad.
            if (puesto == "JR"):
                nombre_jr = nombre
                edad_jr = edad
                bandera_jr = True

            if (bandera_jr == True and edad < edad_jr):
                nombre_jr = nombre
                edad_jr = edad

            # Promedio de edades por género.
            if cont_masc > 0:
                promedio_edad_masc = acumu_edad_masc / cont_masc
            if cont_fem > 0:
                promerio_edad_fem = acumu_edad_fem / cont_fem
            if cont_nb > 0:
                promedio_edad_nb = acumu_edad_nb / cont_nb

        # Cantidad de postulantes complicados
        if cont_post_complejo > 1:
            print (f"El numero de canditatos unicornios es {cont_post_complejo}")
        else:
            print("No se encontraron unicornios en la busqueda")

        # Informar el nombre del progrmamador complicado de encontrar
        if bandera_jr == True:
            print(f"El nombre del programador Jr de menor edad es {nombre_jr}")
        else:
            print("No se encontaron programadores Jr")

        # Informar el promedio de edades por género
        if (cont_masc > 0):
            promedio_edad_masc = acumu_edad_masc / cont_masc
            promedio_edad_masc = round(promedio_edad_masc)
            print(f"El promedio de edad masculina es {promedio_edad_masc}")
        else:
            print("No hay candidatos masculinos")

        if (cont_fem > 0):
            promedio_edad_fem = acumu_edad_fem / cont_fem
            promedio_edad_fem = round(promedio_edad_fem)
            print(f"El promedio de edad feminina es {promedio_edad_fem}")
        else:
            print("No hay candidatos femeninos")

        if (cont_nb > 0):
            promedio_edad_nb = acumu_edad_nb / cont_nb
            promedio_edad_nb = round(promedio_edad_nb)
            print(f"El promedo de edad de persones nb es {promedio_edad_nb}")
        else:
            print("No hay candidates de genere NB")
        

        # Informar la tecno con mas postulantes
        if cont_asp > cont_js and cont_asp > cont_python:
            print("ASP.NET tiene más postulantes")
        elif cont_js > cont_asp and cont_js > cont_python:
            print("JS tiene más postulantes")
        else:
            print("Python tiene más postulantes")

        # Porcentaje de postulantes de cada genero.
        porcentaje_masc = (cont_masc / 10) * 100
        porcentaje_masc = round(porcentaje_masc)
        porcentaje_fem = (cont_fem / 10) * 100
        porcentaje_fem = round(porcentaje_fem)
        porcentaje_nb = (cont_nb / 10) * 100
        porcentaje_nb = round(porcentaje_nb)
        resultado_porcentaje_genero = (
            f"El porcentaje de hombres es de {porcentaje_masc}%\n"
            f"El porcentaje de mujeres es de {porcentaje_fem}%\n"
            f"El porcentaje de persones nb es de {porcentaje_nb}%\n"
        )


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
