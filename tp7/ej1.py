"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""

def cantidad_digitos(n):

    if n < 0:

        n = -n

    # Caso base
    if n < 10:

        return 1

    
    return 1 + cantidad_digitos(n // 10)


# Bloque principal
if __name__ == "__main__":
    numero = int(input("Ingrese un numero entero: "))
    print("Cantidad de digitos:", cantidad_digitos(numero))
