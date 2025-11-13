"""
Escribir una función filtrar_palabras() 
que reciba una cadena de caracteres conteniendo una frase y un entero N, y 
devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. 
Hacer tres versiones de la función, para cada uno de los siguientes casos:

a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filte
"""

def filtrar_palabras(frase, n, op) -> str:

    palabras = frase.split()

    if op == "ciclos":

        resultado = []

        for palabra in palabras:

            if len(palabra) >= n:
                resultado.append(palabra)

        return " ".join(resultado)

    elif op == "comprension":

        return " ".join([p for p in palabras if len(p) >= n])

    elif op == "filter":

        return " ".join(filter(lambda p: len(p) >= n, palabras))

    else:

        return "Opcion incorrecta."


def main() -> None:

    frase = input("Ingrese una frase: ")

    n = int(input("Ingrese la longitud minima: "))

    while True:
        print("1. Filtrar usando ciclos normales")
        print("2. Filtrar usando listas por comprensión")
        print("3. Filtrar usando filter()")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            print("\nResultado:", filtrar_palabras(frase, n, "ciclos"))

        elif opcion == "2":

            print("\nResultado:", filtrar_palabras(frase, n, "comprension"))

        elif opcion == "3":

            print("\nResultado:", filtrar_palabras(frase, n, "filter"))

        elif opcion == "4":

            print("Saliendo...")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
