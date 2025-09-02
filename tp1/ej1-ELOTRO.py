"""
Desarrollar también un programa para ingresar los tres valores, invocar a la función y 
mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""

def informar_el_mayor(a: int, b: int, c:int ) -> int:

    numeros = [a, b, c]

    mayor = max(numeros)

    if numeros.count(mayor) != 1:

        return "El mayor estricto no ha sido encontrado."
    
    return mayor

a = int(input("Ingrese el primer numero: "))

b = int(input("Ingrese el segundo numero: "))

c = int(input("Ingrese el tercer numero: "))

# BLoque principal
print(informar_el_mayor(a, b, c))