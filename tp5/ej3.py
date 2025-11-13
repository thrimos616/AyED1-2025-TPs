"""
Desarrollar una funcion que devuelva una cadena con el nombre del mes cuyo
numero se recibe como parametro. Los nombres de los meses deberan obtenerse de
una lista inicializada dentro de la funcion. Devolver una cadena vacia si el numero
de mes es invalido. La deteccion de meses invalidos debera realizarse con excepciones.
"""

def obtener_nombre_mes(numero_mes: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al numero recibido.
    Si el numero es invalido, devuelve una cadena vacia.
    """

    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    try:

        if numero_mes < 1 or numero_mes > 12:

            raise IndexError("Numero de mes fuera de rango.")

        return meses[numero_mes - 1]

    except IndexError as e:

        print("Error:", e)

        return ""

# BLoque princiapl
print(obtener_nombre_mes(5))
print(obtener_nombre_mes(15))

