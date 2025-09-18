"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. 

El proceso deberá realizarse utilizando la función filter(). 
Imprimir las dos listas por pantalla.
"""

import random as rn

lista_azar = [rn.randint(1, 100) for x in range(20)]

lista_impares = [x for x in lista_azar if x % 2]

print(lista_azar)
print(lista_impares)