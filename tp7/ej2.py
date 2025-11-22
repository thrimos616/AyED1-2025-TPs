"""
Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal.
"""

def binario_a_decimal(n):

    # Caso base
    if n == 0 or n == 1:
        return n

    ultimo = n % 10

    resto = n // 10

    return ultimo + 2 * binario_a_decimal(resto)


# Bloque principal
if __name__ == "__main__":
    numero = int(input("Ingrese un numero binario: "))
    print("Equivalente decimal:", binario_a_decimal(numero))
