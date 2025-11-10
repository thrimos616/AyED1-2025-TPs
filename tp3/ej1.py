"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
ción:

a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.

b. Ordenar en forma ascendente cada una de las filas de la matriz.

c. Intercambiar dos filas, cuyos números se reciben como parámetro.

d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.

e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)

f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.

g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
mero se recibe como parámetro.

h. Determinar si la matriz es simétrica con respecto a su diagonal principal.

i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.

j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.

NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado.
"""

def cargar_ints() -> list[list[int]]:

    matriz_ints = [[0 for num in range(4)] for num in range(4)]
    for lista in matriz_ints:
        print(*matriz_ints)


    """for x in range(n1, n2):
        
        num = int(input("Ingrese un numero: "))

        matriz_ints[x].append(num)"""

    return matriz_ints

# Intento de paip

def crear_matriz(n: int) -> list[list[int]]:
    return [[0 for i in range(n)] for j in range(n)]

# Opcion a
def cargar_matriz(matriz: list[list[int]]) -> list[list[int]]:
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            num = int(input("Ingrese un numero para agregar a la matriz: "))
            matriz[i][j] = num
    return matriz

# Opcion b
def ordenar_filas(matriz: list[list[int]]):
    for fila in matriz:
        fila.sort()
    return matriz

# Opcion c
def intercambiar_filas(matriz, fila_1, fila_2):
    matriz[fila_1], matriz[fila_2] = matriz[fila_2], matriz[fila_1]
    return matriz

# Opcion d
def intercambiar_columnas(matriz, columa_1, columna_2):
    for fila in matriz:
        fila[columa_1], fila[columna_2] = fila[columna_2], fila[columa_1]     
    return matriz

# Opcion e
def transponer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = matriz[j][i]
    return matriz

# Opcion f
def promedio_fila(matriz, fila_jijo):
    promedio = [sum(fila) / len(fila) for fila in matriz if fila == matriz[fila_jijo] and len(fila) > 0]
    return promedio


def main():
    n = int(input("Ingrese la longitud de la matriz: "))

    matriz = crear_matriz(n)

    while True:
        op = input("Ingrese una opcion: ")
        match op:
            case "a": # a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.
                matriz = cargar_matriz(matriz)
                for fila in matriz:
                    print(fila)

            case "b": # b. Ordenar en forma ascendente cada una de las filas de la matriz.
                matriz_ordenada = ordenar_filas(matriz)
                for fila in matriz_ordenada:
                    print(fila)

            case "c": # c. Intercambiar dos filas, cuyos números se reciben como parámetro.
                matriz_filas_intercambiadas = intercambiar_filas(matriz, 0, 2)
                for fila in matriz:
                    print(fila)

            case "d": # d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
                matriz_columnas_intercambiadas = intercambiar_columnas(matriz, 0, 2)
                for fila in matriz:
                    print(fila)

            case "e": # e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
                matriz_transpuesta = transponer_matriz(matriz)
                for fila in matriz:
                    print(fila)

            case "f": # f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
                promedio = promedio_fila(matriz, 0)
                print(*promedio)

            case "g":
                pass
            case "h":
                pass
            case "i":
                pass
            case "j":
                pass
            case "z":
                break
            case _:
                print("Opcion incorrecta.")
                continue

main()