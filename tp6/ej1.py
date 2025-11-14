"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre"
y guarde en el archivo ARMENIA.TXT los registros cuyo apellido termina en "IAN",
en ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los terminados en "EZ".
Descartar el resto.
"""

def clasificar_apellidos(nombre_archivo: str):
    """
    Lee un archivo de texto con nombres y apellidos y los clasifica segun su terminacion.
    Crea tres archivos nuevos: ARMENIA.TXT, ITALIA.TXT y ESPANA.TXT.
    """

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as f:

            for linea in f:

                linea = linea.strip()

                if not linea:
                    continue

                apellido = linea.split(",")[0].strip().upper()

                if apellido.endswith("IAN"):

                    with open("ARMENIA.TXT", "a", encoding="utf-8") as arm:
                        arm.write(linea + "\n")

                elif apellido.endswith("INI"):

                    with open("ITALIA.TXT", "a", encoding="utf-8") as ita:
                        ita.write(linea + "\n")

                elif apellido.endswith("EZ"):
                    
                    with open("ESPANA.TXT", "a", encoding="utf-8") as esp:
                        esp.write(linea + "\n")

    except FileNotFoundError:

        print("No se encontro el archivo.")

    except Exception as e:

        print("Error general:", e)

# Bloque principal
clasificar_apellidos("nombres.txt")
