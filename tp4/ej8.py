"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""

def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los ultimos caracteres (n) de la cadena dada.
    """

    if n > len(cadena):

        n = len(cadena)
    
    subcadena = ""

    for i in range(len(cadena) - n, len(cadena)):

        subcadena += cadena[i]

    return subcadena


# Bloque principal
texto = "El numero de telefono es 2284-4997"
n = 9
resultado = ultimos_caracteres(texto, n)
print(resultado)
