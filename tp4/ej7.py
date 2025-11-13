"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:

a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

# a
def eliminar_subcadena(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena usando rebanadas, dada la posicion inicial y la cantidad de caracteres.
    """

    nueva_cadena = cadena[:posicion] + cadena[posicion + cantidad:]

    return nueva_cadena

# b
def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    Elimina una subcadena sin usar rebanadas, dada la posicion inicial y la cantidad de caracteres.
    """
    
    nueva_cadena = ""

    for i in range(len(cadena)):

        if i < posicion or i >= posicion + cantidad:

            nueva_cadena += cadena[i]

    return nueva_cadena


# Bloque principal

# a
texto = "El numero de telefono es 4356-7890"
resultado = eliminar_subcadena(texto, 25, 9)
print(resultado)

# b
texto = "El numero de telefono es 4356-7890"
resultado = eliminar_subcadena_sin_rebanadas(texto, 25, 9)
print(resultado)
