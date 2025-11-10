'''
Los numeros de claves de dos cajas fuertes estan intercalados dentro de un numero
entero llamado "clave maestra", cuya longitud no se conoce. 

Realizar un programa para obtener ambas claves, donde la primera se construye con los digitos ubicados
en posiciones impares de la clave maestra y la segunda con los digitos ubicados en
posiciones pares. LOs digitos se numeran desde la izquierda.

Ejemplo: Si clave maestra fuera 18293, la clase 1 seria 123 y la clave 2 seria 89
'''

clave_maestra = [1, 8, 2, 9, 3]

clave1 = []

clave2 = [] 

for x in range(len(clave_maestra)):

    if x % 2 == 0:

        clave1.append(clave_maestra[x])
        
    elif x % 2:

        clave2.append(clave_maestra[x])

print(clave1)

print(clave2)