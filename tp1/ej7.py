"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado.

Utilizando esta función sin modificaciones ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""


def diasiguiente(dia: int, mes: int, anio: int) -> tuple:

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    if bisiesto:

        dias_por_mes[1] = 29 
    

    if mes < 1 or mes > 12:

        return "Mes invalido."

    if dia < 1 or dia > dias_por_mes[mes - 1]:

        return "Dia invalido."
    

    if dia < dias_por_mes[mes - 1]:
        
        dia += 1
    
    else:

        dia = 1

        if mes == 12:

            mes = 1
            anio += 1
        
        else:
            
            mes += 1
    
    return dia, mes, anio

# Bloque principal

print(diasiguiente(12, 12, 2005)) # prueba dia

print(diasiguiente(31, 3, 1990)) # prueba mes

print(diasiguiente(31, 12, 2005)) # prueba an;o

