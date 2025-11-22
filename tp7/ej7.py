"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Má-
ximo Común Divisor (también llamado Divisor Común Mayor) basándose en las si-
guientes propiedades:
MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
Utilizando la función anterior calcular el MCD de todos los elementos de una lista de
números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
utilizar iteraciones en ninguna etapa del proceso.
"""


def mcd(x: int, y: int) -> int:

    if x < 0 or y < 0:
        raise ValueError("Los numeros deben ser no negativos.")

    if x == 0:
        return y

    if y == 0:
        return x

    if x == y:
        return x

    if x > y:
        return mcd(x - y, y)

    else:
        return mcd(x, y - x)


def mcd_lista(lista: list[int]) -> int:

    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacia.")

    return mcd_lista_por_index(lista, 0)


def mcd_lista_por_index(lista: list[int], indice: int) -> int:

    if indice == len(lista) - 1:
        return lista[indice]


    actual = lista[indice]
    resto = mcd_lista_por_index(lista, indice + 1)


    return mcd(actual, resto)


# Bloque principal

print("mcd(48, 18) =", mcd(48, 18))     # 6
print("mcd(7, 7) =", mcd(7, 7))         # 7
print("mcd(0, 5) =", mcd(0, 5))         # 5

print("mcd_lista([48, 18, 6]) =", mcd_lista([48, 18, 6]))   # 6
print("mcd_lista([27, 36, 45, 54]) =", mcd_lista([27, 36, 45, 54]))  # 9
print("mcd_lista([0, 20, 30]) =", mcd_lista([0, 20, 30]))   # 10
