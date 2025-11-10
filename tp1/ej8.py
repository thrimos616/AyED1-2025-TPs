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

def imprimir_calendario(mes, anio) -> list[int]:

    calendario = []
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):

        dias_por_mes[1] = 29
    

    primer_dia = diadelasemana(1, mes, anio)
    

    for i in range(primer_dia):

        calendario.append(0)
    

    for dia in range(1, dias_por_mes[mes-1] + 1):

        calendario.append(dia)
    
    return calendario

def mostrar_calendario(mes, anio):

    dias_semana = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"]
    lista_calendario = imprimir_calendario(mes, anio)
    
    print(f"\nCalendario para {mes}/{anio}")

    for dia in dias_semana:

        print(f"{dia:4}", end="")

    print()
    

    contador = 0
    for dia in lista_calendario:

        if dia == 0:

            print("    ", end="")

        else:

            print(f"{dia:4}", end="")
        
        contador += 1

        if contador % 7 == 0:

            print()

# Bloque principal
print(diadelasemana(12, 12, 2005))
mostrar_calendario(12, 2005)