"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comporta-
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:

a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

# a
def extraer_subcadena_rebanada(cadena: str, posicion: int, cantidad: int) -> str: 
    """
    Devuelve una subcadena usando rebanadas, a partir de una posicion y cantidad dadas.
    """

    return cadena[posicion:posicion + cantidad]


# b
def extraer_subcadena_sin_rebanada(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Devuelve una subcadena sin usar rebanadas, a partir de una posicion y cantidad dadas.
    """

    subcadena = ""

    for i in range(posicion, posicion + cantidad):

        if i < len(cadena):

            subcadena += cadena[i]

    return subcadena


# Bloque principal

# a
texto = "El numero de telefono es 4356-7890"
subcadena = extraer_subcadena_rebanada(texto, 25, 9)
print(subcadena)

# b
texto = "El numero de telefono es 4356-7890"
subcadena = extraer_subcadena_sin_rebanada(texto, 25, 9)
print(subcadena)