'''
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.
'''

def printear_cadena(cadena: str):
    mitad = "-" * int((80 - len(cadena)) / 2)
    print(f"{mitad}{cadena}{mitad}")


def main():
    string = "Hola mi nombre es Ezequiel Ricciardi"
    printear_cadena(string)

main()