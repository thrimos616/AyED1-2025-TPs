"""
Desarrollar una funcion para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. 
Tener en cuenta que solo deben reemplazarse palabras completas, y no fragmentos de palabras. 
Escribir tambien un programa para verificar el comportamiento de la funcion.
"""

def reemplazar_palabras(cadena: str, palabra_buscar: str, palabra_nueva: str) -> tuple[str, int]:

    palabras = cadena.split()
    contador = 0
    nueva_lista = []

    for x in palabras:

        if x == palabra_buscar:

            nueva_lista.append(palabra_nueva)
            contador += 1
        
        else:

            nueva_lista.append(x)
    
    nueva_cadena = " ".join(nueva_lista)

    return nueva_cadena, contador


# Bloque principal
texto = "El sol brilla y el sol calienta mucho"
resultado, cantidad = reemplazar_palabras(texto, "sol", "astro")
print("Cadena resultante:", resultado)
print("Cantidad de reemplazos:", cantidad)
