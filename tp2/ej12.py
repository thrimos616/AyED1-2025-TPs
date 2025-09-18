"""
Resolver el siguiente problema, utilizando funciones:

Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. 

Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.

b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. 

Informar cuántos ingresos se eliminaron
"""

def registrar_ingresos():

    ingresos = []
    
    while True:

        num_socio = int(input("Ingrese el numero de socio (5 digitos, 0 para finalizar): "))
        
        if num_socio == 0:

            break
            
        if 10000 <= num_socio <= 99999:

            ingresos.append(num_socio)
        
        else:

            print("Numero de socio invalido.")
    
    return ingresos

def informe_frecuencia(ingresos):
    
        socios_visitados = []
    
        for socio in ingresos:

            if socio not in socios_visitados:

                frecuencia = 0

                for ingreso in ingresos:

                    if ingreso == socio:

                        frecuencia += 1

                print(f"Socio {socio}: {frecuencia} ingreso/s")

                socios_visitados.append(socio)

def eliminar_socio_baja(ingresos):
    
    print("Registros de entrada antes de eliminar:")

    for i in range(len(ingresos)):

        print(f"{i+1} | Socio: {ingresos[i]}")
    
    socio_eliminar = int(input("\nIngrese el numero de socio a dar de baja: "))
    
    ingresos_eliminar = 0
    ingresos_actualizados = []
    
    for socio in ingresos:

        if socio == socio_eliminar:

            ingresos_eliminar += 1

        else:

            ingresos_actualizados.append(socio)
    
    print(f"\nRegistros de entrada despues de eliminar al socio: {socio_eliminar}")
    
    for i in range(len(ingresos_actualizados)):

        print(f"{i+1} | Socio: {ingresos_actualizados[i]}")
    
    print(f"\nSe eliminaron {ingresos_eliminar} ingreso/s del socio {socio_eliminar}")
    
    return ingresos_actualizados, ingresos_eliminar

def main():

    ingresos = registrar_ingresos()
    
    informe_frecuencia(ingresos)
    
    if ingresos:

        ingresos, eliminados = eliminar_socio_baja(ingresos)
        
        if ingresos:

            informe_frecuencia(ingresos)

        else:
            print("\nNo hay ingresos registrados despues de la eliminacion.")


if __name__ == "__main__":
    main()