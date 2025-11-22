"""
Escribir una función que devuelva la suma de los N primeros números naturales.
"""

def suma_naturales(n):

    # Caso base
    if n <= 1:
        
        return n


    return n + suma_naturales(n - 1)


# Bloque principal
if __name__ == "__main__":
    numero = int(input("Ingrese un numero natural: "))
    print("Suma de los primeros", numero, "numeros naturales:", suma_naturales(numero))
