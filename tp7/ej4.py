"""
Desarrollar una función que devuelva el producto de dos números enteros por su-
mas sucesivas.
"""

def producto_enteros(a, b):


    # Caso base
    if b == 0:
        return 0

    if b < 0:
        return -producto_enteros(a, -b)

    return a + producto(a, b - 1)


# Bloque principal
if __name__ == "__main__":
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    print("El producto es:", producto_enteros(x, y))
