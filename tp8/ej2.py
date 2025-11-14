"""
Escribir una funcion que reciba como parametro una tupla conteniendo una fecha
(dia, mes, anio) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La funcion debe contemplar que el anio se ingrese en dos digitos,
los que seran interpretados segun un anio de corte definido dentro del programa.
Cualquier anio mayor que este se considerara del siglo pasado.
"""

def fecha_extendida(fecha):
    """
    Recibe una tupla (dia, mes, anio) y devuelve una cadena con la fecha en formato extendido.
    Interpreta los anios de dos digitos segun un anio de corte (30).
    """

    dia, mes, anio = fecha

    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    corte = 30
    if anio < 100:

        if anio > corte:
            anio += 1900

        else:

            anio += 2000

    return f"{dia} de {meses[mes - 1]} de {anio}"


if __name__ == "__main__":

    d = int(input("Dia: "))
    m = int(input("Mes: "))
    a = int(input("Anio (2 o 4 digitos): "))
    
    print(fecha_extendida((d, m, a)))
