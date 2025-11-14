"""
Se dispone de dos formatos diferentes de archivos de texto con datos de empleados.
El programa debe convertirlos a formato CSV.
Formato 1: Campos de longitud fija.
Formato 2: Cada campo precedido por un numero de dos digitos que indica su longitud.
"""

def convertir_formato1(nombre_archivo: str, salida_csv: str):
    """
    Convierte un archivo de formato 1 (longitud fija) a formato CSV.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as f, open(salida_csv, "w", encoding="utf-8") as out:

        for linea in f:

            partes = linea.strip().split()

            if len(partes) >= 3:

                apellido_nombre = " ".join(partes[:-2])
                fecha = partes[-2]
                domicilio = partes[-1]
                out.write(f"{apellido_nombre},{fecha},{domicilio}\n")

def convertir_formato2(nombre_archivo: str, salida_csv: str):
    """
    Convierte un archivo de formato 2 (longitud variable) a formato CSV.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as f, open(salida_csv, "w", encoding="utf-8") as out:

        for linea in f:

            i = 0
            campos = []

            while i < len(linea):

                if not linea[i:i+2].isdigit():
                    break

                longitud = int(linea[i:i+2])
                i += 2
                campo = linea[i:i+longitud].strip()
                campos.append(campo)
                i += longitud

            out.write(",".join(campos) + "\n")

# Bloque principal
# convertir_formato1("empleados1.txt", "salida1.csv")
# convertir_formato2("empleados2.txt", "salida2.csv")
