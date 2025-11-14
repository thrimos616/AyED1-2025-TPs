"""
Un hotel necesita un programa para gestionar sus habitaciones.
El hotel tiene 10 pisos y 6 habitaciones por piso.
Se deben registrar huespedes y luego mostrar estadisticas.
"""

def registrar_huespedes(nombre_archivo: str):
    """
    Registra huespedes en un archivo CSV hasta que se ingrese DNI -1.
    """

    with open(nombre_archivo, "w", encoding="utf-8") as f:

        while True:

            try:

                dni = int(input("Ingrese DNI (-1 para terminar): "))

                if dni == -1:
                    break

                nombre = input("Apellido y nombre: ")
                ingreso = input("Fecha de ingreso (DDMMAAAA): ")
                egreso = input("Fecha de egreso (DDMMAAAA): ")
                ocupantes = int(input("Cantidad de ocupantes: "))

                if int(egreso) <= int(ingreso):
                    print("La fecha de egreso debe ser posterior.")
                    continue

                f.write(f"{dni},{nombre},{ingreso},{egreso},{ocupantes}\n")

            except ValueError:

                print("Dato invalido.")

# Bloque principal
registrar_huespedes("huespedes.csv")
