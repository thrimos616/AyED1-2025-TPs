"""
Realizar una funcion que reciba como parametros dos cadenas de caracteres
conteniendo numeros reales, sume ambos valores y devuelva el resultado como un
numero real. Devolver -1 si alguna de las cadenas no contiene un numero valido,
utilizando manejo de excepciones para detectar el error.
"""

def sumar_cadenas_numericas(cad1: str, cad2: str) -> float:
    """
    Suma dos numeros reales representados como cadenas.
    Devuelve -1 si alguna de las cadenas no es valida.
    """

    try:

        num1 = float(cad1)
        num2 = float(cad2)

        return num1 + num2

    except ValueError:
        
        return -1

# BLoque principal
print(sumar_cadenas_numericas("3.5", "2.7"))
print(sumar_cadenas_numericas("abc", "2"))

