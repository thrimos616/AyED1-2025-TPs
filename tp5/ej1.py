"""
Desarrollar una funcion para ingresar a traves del teclado un numero natural.
La funcion rechazara cualquier ingreso invalido de datos utilizando excepciones
y mostrara la razon exacta del error. Controlar que se ingrese un numero, que ese
numero sea entero y que sea mayor que 0, mostrando un mensaje con la razon
exacta del error en caso necesario. Devolver el valor ingresado cuando este sea
correcto. Escribir tambien un programa que permita probar el correcto funcionamiento de la misma.
"""

def ingresar_numero_natural() -> int:
    """
    Solicita al usuario un numero natural y valida que sea entero y mayor a cero.
    Muestra mensajes de error especificos segun el tipo de excepcion.
    """

    while True:

        try:
            
            valor = input("Ingrese un numero natural: ")
            numero = int(valor)

            if numero <= 0:

                raise ValueError("El numero debe ser mayor que 0.")

            return numero

        except ValueError as e:

            print("Error:", e)

        except Exception as e:

            print("Error general:", e)

# Bloque principal
n = ingresar_numero_natural()
print("Numero ingresado:", n)

