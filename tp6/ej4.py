"""
Desarrollar un programa para eliminar todos los comentarios de un programa
Python. Los comentarios comienzan con # (siempre que no este dentro de comillas)
y los docstrings tambien deben eliminarse.
"""

def eliminar_comentarios(nombre_archivo: str, salida: str):
    """
    Elimina comentarios y docstrings de un archivo Python y genera una version limpia.
    """

    try:

        with open(nombre_archivo, "r", encoding="utf-8") as f, open(salida, "w", encoding="utf-8") as out:
            dentro_doc = False

            for linea in f:

                linea = linea.rstrip("\n")

                # Docstrings
                if '"""' in linea or "'''" in linea:

                    dentro_doc = not dentro_doc
                    continue

                if dentro_doc:
                    continue

                # Comentarios una linea

                if "#" in linea:

                    pos = linea.find("#")

                    if pos != -1:
                        linea = linea[:pos]

                if linea.strip() != "":
                    out.write(linea.rstrip() + "\n")

    except FileNotFoundError:

        print("Archivo no encontrado.")

    except Exception as e:

        print("Error general:", e)

# Bloque principal
eliminar_comentarios("programa.py", "sin_comentarios.py")
