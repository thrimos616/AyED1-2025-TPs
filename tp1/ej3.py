"""
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. 
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) 
se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y 
devuelva el total gastado en viajes. 
Realizar también un programa para verificar el comportamiento de la función.
"""

def gasto_viajes_mes(n: int) -> int:

    total_gastado = 0

    precio_base = 1031

    if 1 < n <= 20:

        total_gastado = precio_base * n

        return total_gastado

    elif 21 <= n <= 30:

        total_gastado = (precio_base * n) * (1 - 20 / 100)

        return total_gastado
    
    elif 31 <= n <= 40:

        total_gastado = (precio_base * n) * (1 - 30 / 100)

        return total_gastado

    elif n > 40:

        total_gastado = (precio_base * n) * (1 - 40 / 100)

        return total_gastado

    else:

        return "El numero es invalido."

# Bloque principal

cant_viajes = int(input("Ingrese la cantidad de viajes realizados este mes: "))

print(gasto_viajes_mes(cant_viajes))