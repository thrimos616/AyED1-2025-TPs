"""
Se solicita crear un programa para leer direcciones de correo electronico y verificar
si representan una direccion valida. Por ejemplo usuario@dominio.com.ar. 
Para que una direccion sea considerada valida:
- El nombre de usuario debe poseer solamente caracteres alfanumericos
- La direccion debe contener un solo caracter @
- El dominio debe tener al menos un caracter
- Debe finalizar con .com o .com.ar

Repetir el proceso de validacion hasta ingresar una cadena vacia.
Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabeticamente,
recordando que las direcciones de mail no distinguen mayusculas ni minusculas.
"""

def validar_mail(mail: str) -> bool:
    """
    Verifica si una direccion de correo electronico es valida segun las siguientes reglas:
    - Contiene solo un caracter '@'
    - El usuario tiene solo caracteres alfanumericos
    - El dominio termina en .com o .com.ar
    - El dominio tiene al menos un caracter antes del punto
    Retorna True si el mail es valido, False en caso contrario.
    """

    mail = mail.lower().strip()

    if mail.count("@") != 1:

        return False

    usuario, dominio = mail.split("@")

    if not usuario.isalnum():

        return False

    if not dominio.endswith(".com") and not dominio.endswith(".com.ar"):

        return False

    if dominio.startswith(".") or len(dominio.replace(".com", "").replace(".ar", "")) == 0:

        return False

    return True


def mostrar_dominios(dominios: list[str]) -> None:
    """
    Muestra por pantalla los dominios ordenados alfabeticamente.
    """

    print("\nDominios registrados (ordenados):")

    for d in sorted(dominios):

        print("-", d)


def main():
    """
    Lee direcciones de correo hasta ingresar una cadena vacia.
    Valida las direcciones y muestra los dominios unicos ordenados alfabeticamente.
    """

    dominios = []

    while True:
        correo = input("Ingrese un correo electronico (Enter para salir): ").strip()

        if correo == "":
            break

        if validar_mail(correo):

            print("Direccion valida.")
            dominio = correo.lower().split("@")[1]

            if dominio not in dominios:

                dominios.append(dominio)
        else:

            print("Direccion invalida.")

    mostrar_dominios(dominios)


# Bloque principal
main()
