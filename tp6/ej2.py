"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electronico. El tamaño maximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben incluir un sufijo
que indique de que parte se trata. No se debe dividir un registro a la mitad.
"""

def dividir_archivo(nombre_archivo: str, tam_max: int):
    """
    Divide un archivo de texto en varias partes sin cortar lineas.
    Cada parte tiene un tamaño maximo indicado por el usuario.
    """

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as f:

            parte = 1
            tam_actual = 0
            salida = open(f"{nombre_archivo}_parte{parte}.txt", "w", encoding="utf-8")

            for linea in f:

                if tam_actual + len(linea) > tam_max:

                    salida.close()
                    parte += 1
                    tam_actual = 0
                    salida = open(f"{nombre_archivo}_parte{parte}.txt", "w", encoding="utf-8")

                salida.write(linea)
                tam_actual += len(linea)

            salida.close()

            print(f"Archivo dividido en {parte} partes.")

    except FileNotFoundError:

        print("Archivo no encontrado.")

    except Exception as e:

        print("Error general:", e)

# Bloque principal
dividir_archivo("texto.txt", 200)
