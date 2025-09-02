"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. 
Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. 
Realizar también un programa para verificar el comportamiento de la función.
"""


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    
    if not (1 <= mes <= 12):
        return False

    if not (1 <= anio <= 2025):
        return False

    bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    dias_por_mes = {

        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    if bisiesto:
        dias_por_mes[2] = 29

    if not (1 <= dia <= dias_por_mes[mes]):
        return False

    return True

# Bloque principal

dia = int(input("Ingrese un dia: "))

mes = int(input("Ingrese un mes: "))

anio = int(input("Ingrese un anio: "))