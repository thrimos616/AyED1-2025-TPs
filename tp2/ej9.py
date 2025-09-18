"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""

a = int(input("Ingrese el primer numero del rango: "))

b = int(input("Ingrese el segundo numero del rango: "))

multiplos_siete = [i for i in range(a, b) if i % 7 == 0 and i % 5]

print(multiplos_siete)