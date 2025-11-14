"""
Desarrollar un programa que utilice una funcion que reciba como parametro una cadena 
conteniendo una direccion de correo electronico y devuelva una tupla con las distintas 
partes que la componen. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar)
La funcion debe detectar formatos invalidos y devolver una tupla vacia.
"""

def descomponer_email(correo):
    """
    Recibe una direccion de correo y devuelve una tupla con sus partes separadas.
    Si el formato es invalido, devuelve una tupla vacia.
    """

    if "@" not in correo or correo.count("@") != 1:
        return ()

    usuario, dominio = correo.split("@")

    if "." not in dominio or not usuario:
        return ()

    partes = [usuario] + dominio.split(".")

    return tuple(partes)


if __name__ == "__main__":
    
    email = input("Ingrese un correo electronico: ")
    print(descomponer_email(email))
