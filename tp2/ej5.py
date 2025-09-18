"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. 

Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. 
Desarrollar además un programa para verificar el comportamiento de la función
"""

def verificar_ordenada(lista: list[int]) -> bool:

    return True if lista == sorted(lista) else False

# Bloque pricipal

lista_chida = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_no_chida = [3, 2, 1, 0]

print(verificar_ordenada(lista_chida))
print(verificar_ordenada(lista_no_chida))