"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). 
Devolver -1 en caso de no haber ninguno. 
No utilizar operadores lógicos (and, or, not). 
"""

def informar_el_mayor(a: int, b: int, c:int ) -> None:

    numeros = [a, b, c]

    mayor = max(numeros)

    if numeros.count(mayor) == 1:

        return mayor
    
    return -1 

    
# Bloque principal
print(informar_el_mayor(3, 7, 1))
print(informar_el_mayor(5, 5, 2)) 
print(informar_el_mayor(4, 4, 4))