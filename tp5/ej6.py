"""
El metodo index permite buscar un elemento dentro de una lista, devolviendo la
posicion que ocupa. Si no pertenece a la lista se produce una excepcion ValueError.
Desarrollar un programa que cargue una lista con numeros enteros ingresados
(terminando con -1) y permita buscar elementos. Si no se encuentra el valor,
mostrar error. Abortar al tercer error detectado. No usar 'in'.
"""

def buscar_en_lista():
    """
    Permite al usuario crear una lista de enteros y buscar valores dentro de ella.
    Finaliza tras tres errores consecutivos.
    """

    lista = []

    while True:

        try:

            num = int(input("Ingrese un numero (-1 para terminar): "))

            if num == -1:
                break

            lista.append(num)

        except ValueError:

            print("Debe ingresar un numero entero.")

    errores = 0

    while errores < 3:

        try:

            valor = int(input("Ingrese el numero a buscar: "))

            posicion = lista.index(valor)

            print(f"El numero {valor} se encuentra en la posicion {posicion}.")

        except ValueError:

            errores += 1

            print("El numero no se encuentra en la lista.")

    print("Se detectaron tres errores. Programa finalizado.")

# Bloque principal
buscar_en_lista()