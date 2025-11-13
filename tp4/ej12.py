"""
Escribir un programa para crear una lista por comprension con los naipes de la baraja espanola.
La lista debe contener cadenas de caracteres. 
Ejemplo: ["1 Oros", "2 Oros", ...]. 
Imprimir la lista por pantalla.
"""

def crear_baraja() -> list[str]:

    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    baraja = []

    for palo in palos:

        for numero in range(1, 13):

            if numero != 8 and numero != 9:

                carta = str(numero) + " " + palo
                baraja.append(carta)

    return baraja


# Bloque principal
baraja_espanola = crear_baraja()

print(baraja_espanola)
