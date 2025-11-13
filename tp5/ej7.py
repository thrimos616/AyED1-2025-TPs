"""
Escribir un programa que juegue con el usuario a adivinar un numero.
El programa genera un numero al azar entre 1 y 500 y el usuario debe adivinarlo.
Cada vez que se introduce un valor, se indica si el numero buscado es mayor o menor.
Contar los intentos. Si el usuario ingresa algo invalido, mostrar un mensaje y
contar igual el intento.
"""

import random

def juego_adivinar_numero():
    """
    Juega con el usuario a adivinar un numero entre 1 y 500.
    Informa si el numero secreto es mayor o menor.
    """

    numero_secreto = random.randint(1, 500)
    intentos = 0

    while True:

        try:

            intento = int(input("Ingrese un numero entre 1 y 500: "))
            intentos += 1

            if intento < numero_secreto:

                print("El numero secreto es mayor.")

            elif intento > numero_secreto:

                print("El numero secreto es menor.")

            else:
                
                print(f"GANASTE!!! Adivinaste en {intentos} intentos.")
                break

        except ValueError:

            print("Entrada invalida. Se cuenta como un intento.")

            intentos += 1

# Bloque principal
juego_adivinar_numero()

