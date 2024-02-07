# SE importan librerías
# se pone el énfasis en la programación per se, no en Python. Esto es un curso de programación, no de Python.
# Saber algorítmia, y algoritmos básicos

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Manuel
apellido: Fernández Casenave
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

# El class, el def, el if es todo código para hacer correr el programa.
# De "def" para abajo no se toca nada, es el código que configura
# la parte gráfica del programa.

# Generalmente se van una o varias funciones que se ejecutan para hacer correr el progrmaa
# por ejemplo: btn_mostrar_on_click es una función que se ejecuta cuando se hace click en el botón.

class App(customtkinter.CTk):

    # def, if, pass son todas palabras reservadas de Python
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    # Los 4 espacios de indentación son para que el código se ejecute dentro de la función.
    # la identación tiene que estar a la derecha si o si

    # Qué estilo de programación se está usando? Con datos de entrada.
    # Con datos de cualquier fuente: entrada -> proceso -> salida
    # la salida son datos procesados = información
    # Cómo sacamos los datos? Cómo los proecesamos? Cómo los mostramos?
    # - cómo los guardamos? en variables. Esa información (la que se guarda en menmoreia),
    # y se guarda en variable (en un espacio en memoria).
        
    # Si quiero guardar una la edad? Hay restricciones en los nombres de las variables
    # - no puede empezar con un número
    # - no puede tener espacios
    # - no puede tener caracteres especiales
    # - no puede tener tildes

    # La creación y asignación se hacen juntas.
    # Cómo asignamos un valor a una variable? con el signo de igualdad.
    # el operador de asignación es el signo de igualdad " = "
    # el operador de asignación es un operador binario, porque tiene dos operandos.
    # primero se evalúa el lado derecho, y luego se asigna el valor a la variable del lado izquierdo.
    # de esta manera, de derecha a izquierda se asigna el valor a la variable.
    # el operador de igualdad es el doble signo de igualdad " == "
    
    # los nombre de las variables tienen que ser descriptivos, que se entienda qué es lo que guarda.
    # la prioridad es que el código sea legible, que se entienda qué es lo que hace
    # que sea editable, que se pueda modificar, que otros programadores puedan entenderlo.
    # Hacer que el código sea del tipo "Clean Code"

    # Qué es Pep8? Es una guía de estilo para escribir código en Python.
    # Leer las reglas de Pep8, y aplicarlas ej: 4 espacios de identación, 79 caracteres por línea, etc.
    # También hay herramientas que se llaman "linters" que chequean el código y te dicen si está bien o mal.
    # Ej: flake8, pylint, pyflakes, etc.
    # El: guía de estilo -> se agrega esa gúia a un linter, el equipo de trabajo usa ese linter.

    # Ejemplos de Pep8 a seguir:
    # 4 espacios de identación, identación a la derecha, no más de 79 caracteres por línea, etc.

    # Comentarios: son MUY importantes, porque explican qué es lo que hace el código.
    # el interprete de Python ignora los comentarios, no los ejecuta.
    # se usan pero no abusar de ellos, porque sino el código se vuelve menos claro
    # Según Bob Martin, el mejor comentarios es código bien escrito.
    # También, dado que el código cambia, los comentarios se tienen que mantener actualizados,
    # queda código nuevo con comentarios viejos, y eso es peor que no tener comentarios.

    # Cómo COMIENZA el Clean Code? Con nombres de variables descriptivos y representativos
    # Por defecto que Python utilizar el snake_case
    # NO SE ESCRIBE NINGUNA VARIABLES QUE NO ESTÉ EN snake_case

    '''
    El Pep8 nos dice que todo archivo de Pyhton debaría comenzar con un 
    comentario multilinea que explique qué es lo que hace el archivo.
    '''
    # Print es una función que imprime en la consola, no en la pantalla.

    # Tipos de datos: int, float, str, bool, list, tuple, dict, set
    # una variable puede cambiar el tipo de dato.
    # El tipado de datos puede ser dinámico o estático.
    # También el tipo de dato puede ser fuerte o débil, 
    # Python es dinámico y débilmente tipado.
    # Ejemplos de tipos de datos:
    # - int: 1, 2, 3, 4, 5, 999
    # - float: 1.039, 2.220, 2233.0443
    # - str: "hola", "chau", "123"
    # - bool: True, False
    # vacio = None # tipo de dato None, es un tipo de dato que representa la ausencia de valor.

    # Cómo usar datos e interatuar con el usuario?
    # Alert, question y prompt
    # - alert: una función que recibe 
    #  alert("Hola mundo", "Otro mensaje")

    # a partir de aquí se escribe el código que vamos a trabajar
    def btn_mostrar_on_click(self):

        # alert("Esto es un alert", "mensaje del alert")
        # question("Esto es un question", "mensaje del question")

        respuest_prompt = prompt("Ingrese su nombre", "Nombre")

        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
