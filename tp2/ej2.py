"""
Escribir funciones para:

a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.

Combinar estas tres funciones en un mismo programa.
"""

import random as rn 

def lista_elementos_azar(n: int):

    lista = []

    for x in range(n):

        numero_azar = rn.randint(1, 100)

        lista.append(numero_azar)
    
    return lista

def elemento_repetido(lista: list[int]):

    repetido = False

    for x in lista:

        if lista[x] == x:

            repetido = True

    return repetido

def elementos_unicos(lista: list[int]):

    lista_unicos = []

    for x in lista:

        if lista[x] != x:

            lista_unicos.append(x)

    return lista_unicos

# Bloque principal

# Genera la lista
cantidad = int(input("Ingrese la cantidad de elementos aleatorios: "))

lista = lista_elementos_azar(cantidad)

print("Lista generada:", lista)

# Verifica si hay valores repetidos
hay_repetidos = elemento_repetido(lista)

print("Hay elementos repetidos?:", hay_repetidos)

# Muestra los elementos unicos

unicos = elementos_unicos(lista)

print("Elementos únicos:", unicos)