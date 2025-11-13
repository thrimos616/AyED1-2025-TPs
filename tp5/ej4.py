"""
Todo programa Python es susceptible de ser interrumpido mediante Ctrl-C, lo que
genera una excepcion KeyboardInterrupt. Realizar un programa para imprimir los
numeros entre 1 y 100000, y que solicite confirmacion al usuario antes de detenerse
cuando se presione Ctrl-C.
"""

def imprimir_numeros_con_interrupcion():
    """
    Imprime numeros del 1 al 100000.
    Si se presiona Ctrl-C, pide confirmacion antes de detenerse.
    """

    try:

        for i in range(1, 100001):

            print(i)

    except KeyboardInterrupt:

        confirmar = input("\n¿Desea detener el programa? (s/n): ").lower()

        if confirmar != "s":

            imprimir_numeros_con_interrupcion()

# Bloque principal
imprimir_numeros_con_interrupcion()

