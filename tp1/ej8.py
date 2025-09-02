"""
La siguiente función permite averiguar el día de la semana para una fecha determinada. 
La fecha se suministra en forma de tres parámetros enteros y la función de-
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. 
Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. 
Considerar que la semana comienza en domingo.
"""

def diadelasemana(dia: int, mes: int, anio: int) -> int:

    if mes < 3:

        mes = mes + 10
        anio = anio - 1

    else:

        mes = mes - 2

    siglo = anio // 100

    anio2 = anio % 100

    dia_semana = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    if dia_semana < 0:

        dia_semana = dia_semana + 7

    return dia_semana

def imprimir_calendario(mes, n) -> list[int]:

    calendario = []

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i, x in enumerate(dias_por_mes):

        if mes == i + 1:

            cant_dias_calendario = x * ()

            calendario

        if n > 

        print(x)
        print(len(dias_por_mes))
        
# Bloque principal



print(diadelasemana(12, 12, 2005))