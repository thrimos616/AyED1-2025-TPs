"""
Escribir una funcion que indique si dos fichas de domino encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4).
La funcion devuelve True o False.
"""

def encajan(ficha1, ficha2):
    """
    Recibe dos tuplas representando fichas de domino.
    Devuelve True si encajan (tienen al menos un numero en comun).
    """

    return not set(ficha1).isdisjoint(ficha2)


if __name__ == "__main__":
    
    f1 = (int(input("Ficha 1 lado A: ")), int(input("Ficha 1 lado B: ")))
    f2 = (int(input("Ficha 2 lado A: ")), int(input("Ficha 2 lado B: ")))
    
    print("Encajan:", encajan(f1, f2))
