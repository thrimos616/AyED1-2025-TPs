'''
1. Desarrollar una funcion que determine si una cadena de caracteres es capicua, sin utilizar cadenas auxiliares
ni rebanadas. Escribir ademas un programa que permita verificar su funcionamiento.
'''

def es_capicua(palabra: str):
    n = len(palabra)
    for i in range(len(palabra)):
        if palabra[i] == palabra[n - 1 - i]:
            return True
    return False

def main():
    string = input("Ingrese una cadena de caracteres: ").lower()

    resultado = es_capicua(string)
    print(resultado)

main()
