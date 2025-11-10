"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. 
¿En qué cambiaría la función si el rango de valores fuese diferente?
"""

def numeros_romanos(n: int) -> str:

    try:

        if 0 < n > 4000:

            raise ValueError("Numero fuera de rango.")

        if not isinstance(n, int):

            raise TypeError("Solo se aceptan valores numericos.")

        lista_romanos = [

            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        
        resultado = ""

        for valor, letras in lista_romanos:

            while n >= valor:

                resultado += letras
                n -= valor

        return print(resultado)

    except (TypeError, ValueError) as e:

        print(f"Error: {e}")

# Bloque principal

numeros_romanos(20) # XX
numeros_romanos("s") # False
