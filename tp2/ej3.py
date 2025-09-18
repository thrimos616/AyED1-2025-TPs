"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. 
Luego se solicita imprimir los últimos 10 valores de la lista.
"""

def numeros_cuadrados() -> list[int]:

    lista_cuadrados = []

    n = int(input("Ingrese el numero: "))

    for x in range(1, n):

        lista_cuadrados.append(x * x)
        
    return lista_cuadrados

# BLoque princpal

# Todos los elementos
print(numeros_cuadrados()) 

# Ultimos 10
cuadrado = numeros_cuadrados()

print("Ultimos 10 valores: ", cuadrado[-10:])