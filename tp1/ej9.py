"""
Resolver el siguiente problema utilizando funciones:

Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. 
La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada 
(500 kilogramos).

En un cajón caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. 
Si el peso de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. 

Desarrollar un programa para ingresar la cantidad de naranjas cosechadas e 
informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. 

Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cose-
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo.
"""

import random as rn 

def generar_peso_naranjas(n) -> list[int]:

    peso_naranjas = []

    for i in range(n):

        numero_azar = rn.randint(150, 350)

        peso_naranjas.append(numero_azar)

    return peso_naranjas


def clasificar_naranjas(n) -> str:

    peso_naranjas = generar_peso_naranjas(n)

    naranjas_cajon = []

    naranjas_jugo = []

    for x in peso_naranjas:

        if 200 <= x <= 300: 

            naranjas_cajon.append(x)
        
        else:

            naranjas_jugo.append(x)

    return ( 

        f"Naranjas para cajon ({len(naranjas_cajon)}): {naranjas_cajon}\n"
        f"Naranjas para jugo ({len(naranjas_jugo)}): {naranjas_jugo}"
    )


def determinar_cajones(naranjas_cajon: list[int]) -> tuple[int, int]:

    cajones_llenos = len(naranjas_cajon) // 100

    sobrantes = len(naranjas_cajon) % 100

    return cajones_llenos, sobrantes


def calcular_camiones_necesarios(n) -> str:

    peso_naranjas = generar_peso_naranjas(n)

    peso_total = sum(peso_naranjas) 

    camiones_necesarios = peso_total // 500000  


    if peso_total % 500000 >= 400000 or peso_total >= 500000:

        return f"Se van a despachar un total de {camiones_necesarios} camiones."

    else:

        return "El camión no cumple con la cantidad mínima para ser despachado."


# Bloque principal

print(clasificar_naranjas(20))
print(calcular_camiones_necesarios(2000))
