"""
Muchas aplicaciones financieras requieren que los numeros sean expresados tambien en letras. 
Por ejemplo, el numero 2153 puede escribirse como "dos mil ciento cincuenta y tres". 
Escribir un programa que utilice una funcion para convertir un numero entero entre 0 y 1 billon 
(1.000.000.000.000) a letras. 
¿En que cambiaria la funcion si tambien aceptara numeros negativos? ¿Y numeros con decimales?
"""

def numero_a_letras(n: int) -> str:



    unidades = ["", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
    decenas = ["", "Diez", "Veinte", "Treinta", "Cuarenta", "Cincuenta", 
               "Sesenta", "Setenta", "Ochenta", "Noventa"]
    centenas = ["", "Cien", "Doscientos", "Trescientos", "Cuatrocientos", 
                "Quinientos", "Seiscientos", "Setecientos", "Ochocientos", "Novecientos"]

    if n == 0:

        return "Cero"

    if n < 0:
        return "Menos " + numero_a_letras(-n)

    partes = []

    if n >= 1000:

        miles = n // 1000
        resto = n % 1000

        if miles == 1:

            partes.append("Mil")

        else:
            partes.append(numero_a_letras(miles) + " Mil")

        if resto > 0:

            partes.append(numero_a_letras(resto))

        return " ".join(partes)

    if n >= 100:

        c = n // 100
        resto = n % 100

        if c == 1 and resto > 0:

            partes.append("ciento")

        else:
            partes.append(centenas[c])

        n = resto

    if n >= 10:

        d = n // 10
        u = n % 10

        if u == 0:

            partes.append(decenas[d])

        else:

            partes.append(decenas[d] + " y " + unidades[u])

    elif n > 0:
        
        partes.append(unidades[n])

    return " ".join(partes).strip()


# Bloque principal
numero = int(input("Ingrese un numero entre 0 y 9999: "))
print(numero_a_letras(numero))
