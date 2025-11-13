"""
La raiz cuadrada de un numero puede obtenerse mediante la funcion sqrt() del
modulo math. Escribir un programa que utilice esta funcion para calcular la raiz
cuadrada de un numero cualquiera ingresado a traves del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un numero negativo.
"""

import math

def calcular_raiz_cuadrada():
    """
    Solicita un numero al usuario y calcula su raiz cuadrada.
    Maneja errores si el valor es negativo o no es numerico.
    """

    try:

        valor = float(input("Ingrese un numero: "))

        if valor < 0:

            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")

        print("La raiz cuadrada es:", math.sqrt(valor))

    except ValueError as e:

        print("Error:", e)

    except Exception as e:

        print("Error general:", e)

# Bloque principal
calcular_raiz_cuadrada()

