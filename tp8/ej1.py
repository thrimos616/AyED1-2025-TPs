"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, 
y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha valida.
b. Sumar N dias a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo 
   se considerara que el primero corresponde al dia anterior. En ningun caso la diferencia 
   en horas puede superar las 24 horas.
"""

from datetime import datetime, timedelta


def ingresar_fecha():
    """
    Solicita al usuario una fecha valida en formato DD/MM/AAAA.
    Devuelve una tupla (dia, mes, anio).
    """

    while True:

        fecha_str = input("Ingrese una fecha (DD/MM/AAAA): ")

        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return (fecha.day, fecha.month, fecha.year)

        except ValueError:

            print("Fecha invalida. Intente nuevamente.")


def sumar_dias(fecha, dias):
    """
    Suma N dias a una fecha dada (tupla dia, mes, anio).
    Devuelve una nueva tupla con la fecha resultante.
    """

    dia, mes, anio = fecha
    fecha_obj = datetime(anio, mes, dia)
    nueva_fecha = fecha_obj + timedelta(days=dias)

    return (nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)


def ingresar_horario():
    """
    Solicita al usuario un horario valido en formato HH:MM.
    Devuelve una tupla (hora, minuto).
    """

    while True:

        hora_str = input("Ingrese un horario (HH:MM): ")

        try:

            hora = datetime.strptime(hora_str, "%H:%M")
            return (hora.hour, hora.minute)

        except ValueError:

            print("Horario invalido. Intente nuevamente.")


def diferencia_horas(horario1, horario2):
    """
    Calcula la diferencia entre dos horarios (tuplas (hora, minuto)).
    Si el primer horario es mayor, se asume que pertenece al dia anterior.
    Devuelve la diferencia en horas (float).
    """

    h1, m1 = horario1
    h2, m2 = horario2
    t1 = timedelta(hours=h1, minutes=m1)
    t2 = timedelta(hours=h2, minutes=m2)

    if t1 > t2:
        
        t2 += timedelta(days=1)

    diff = t2 - t1

    return diff.total_seconds() / 3600


# Programa principal
if __name__ == "__main__":

    fecha = ingresar_fecha()
    
    dias = int(input("Ingrese cantidad de dias a sumar: "))
    print("Nueva fecha:", sumar_dias(fecha, dias))

    h1 = ingresar_horario()
    h2 = ingresar_horario()

    print("Diferencia en horas:", diferencia_horas(h1, h2))
