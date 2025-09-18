"""
Desarrollar cada una de las siguientes funciones y escribir un programa que per-
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun-
ción:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen-
tos también será un número al azar de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

import random as rn

def cargar_lista() -> list[int]:   # a

    cant_elementos = rn.randint(10, 99)

    lista = []

    for x in range(cant_elementos):

        numero_azar = rn.randint(1000, 9999)

        lista.append(numero_azar)
    
    return lista

def producto_lista() -> tuple[list[int], int]:

    lista = cargar_lista()

    producto = sum(lista)

    return lista, producto

def eliminar_valor(n) -> list[int]:

    lista = cargar_lista()

    for x in lista:

        if x == n:

            lista.remove(x)

    return lista



# Bloque principal

# print(cargar_lista()) # a

# print(producto_lista())

# print(eliminar_valor(6666))