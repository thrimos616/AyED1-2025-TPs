"""
Realizar una función que devuelva el resto de dos números enteros, utilizando res-
tas sucesivas.
"""

def resto(a, b):

    if b == 0:
        raise ValueError("No se puede dividir por cero")

    if a < 0:
        return -resto(-a, b)

    if b < 0:
        return resto(a, -b)

    # Caso base
    if a < b:
        return a

    return resto(a - b, b)


# Bloque principal
if __name__ == "__main__":
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    print("El resto es:", resto(x, y))
