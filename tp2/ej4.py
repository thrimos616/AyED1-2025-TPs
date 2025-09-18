"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de valores a eliminar y la lista resultante. 
La función debe modificar la lista original sin crear una copia modificada.
"""

def eliminar_valores_lista() -> list[int]:

    lista_primera = [2, 3, 4]

    lista_segunda = [3, 2, 3, 4, 5, 1]

    print(f"Lista original: {lista_segunda}\n")
    print(f"Lista de valores a eliminar: {lista_primera}\n")

    for elem1, elem2 in zip(lista_primera, lista_segunda):

        if elem2 == elem1:

            lista_segunda.remove(elem2)

    print(f"Lista resultante: {lista_segunda}")
    
eliminar_valores_lista()