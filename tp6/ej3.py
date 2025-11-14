"""
Una institucion deportiva necesita clasificar atletas por altura. 
Desarrollar las funciones:
- GrabarRangoAlturas(): graba las alturas de los atletas por deporte.
- GrabarPromedio(): graba el promedio de cada deporte.
- MostrarMasAltos(): muestra los deportes con promedio superior al promedio general.
"""

def GrabarRangoAlturas(nombre_archivo: str):
    """
    Solicita al usuario ingresar deportes y alturas de atletas.
    Graba los datos en un archivo de texto.
    """

    with open(nombre_archivo, "w", encoding="utf-8") as f:

        while True:
            deporte = input("Ingrese el nombre del deporte (o Enter para salir): ")

            if deporte == "":
                break

            f.write(deporte + "\n")

            while True:

                altura = input("Ingrese altura del atleta (o Enter para cambiar de deporte): ")

                if altura == "":
                    break

                f.write(altura + "\n")

def GrabarPromedio(nombre_archivo: str, archivo_prom: str):
    """
    Lee las alturas del archivo anterior y graba los promedios de cada deporte.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as f, open(archivo_prom, "w", encoding="utf-8") as out:

        lineas = f.readlines()
        i = 0

        while i < len(lineas):

            deporte = lineas[i].strip()
            i += 1
            alturas = []

            while i < len(lineas) and lineas[i].strip().isdigit():

                alturas.append(int(lineas[i].strip()))
                i += 1

            if alturas:

                promedio = sum(alturas) / len(alturas)
                
                out.write(f"{deporte}\n{promedio:.2f}\n")

def MostrarMasAltos(archivo_prom: str):
    """
    Muestra los deportes con promedio superior al promedio general.
    """

    with open(archivo_prom, "r", encoding="utf-8") as f:
        lineas = [x.strip() for x in f.readlines()]
        deportes = []
        promedios = []
        for i in range(0, len(lineas), 2):
            deportes.append(lineas[i])
            promedios.append(float(lineas[i + 1]))

        prom_general = sum(promedios) / len(promedios)
        print("Promedio general:", prom_general)
        print("Deportes con promedio superior:")
        for d, p in zip(deportes, promedios):
            if p > prom_general:
                print(d)

# Bloque princpal
# GrabarRangoAlturas("alturas.txt")
# GrabarPromedio("alturas.txt", "promedios.txt")
# MostrarMasAltos("promedios.txt")
