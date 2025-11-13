"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
"""

def ordenar_por_longitud(cadena: str) -> str:

    signos = ",.;:!?¡¿"
    palabras = cadena.split()

    # Limpia las palabras
    lista_palabras = []

    for palabra in palabras:

        palabra_limpia = ""

        # esto tal vez tenga una manera mas eficiente, pero como buen procastinador, no tengo tiempo ;)
        for c in palabra:

            if c not in signos:

                palabra_limpia += c

        lista_palabras.append((palabra, len(palabra_limpia)))
    
    # Se ordenan por longitud con una lambda
    lista_palabras.sort(key=lambda x: x[1])

    
    cadena_ordenada = " ".join([p[0] for p in lista_palabras])

    return cadena_ordenada


# Bloque principal
texto = "Este ejercicio,,, fue hecho mientras sonaba Death! ... como quien dice no?"
resultado = ordenar_por_longitud(texto)
print(resultado)
