"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
porciones relativas que cada elemento tiene en la lista original. 

Desarrollar también un programa que permita verificar el comportamiento de la función. 

Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

def normalizar_lista(lista: list[int]) -> list[float]:

    lista_total = []

    total_elementos = sum(lista)

    for x in lista:

        resultado = (x / total_elementos)

        lista_total.append(resultado)        

    return lista_total

# Bloque principal

lista_chida = [1, 1, 2]

print(normalizar_lista(lista_chida))