"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""

numeros_impares = [x for x in range(100, 201) if x % 2 == 0]

print(numeros_impares)