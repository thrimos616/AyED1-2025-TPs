"""
Resolver el siguiente problema, diseñando las funciones a utilizar:

Una clínica necesita un programa para atender a sus pacientes. 
Cada paciente que ingresa se anuncia en la recepción indicando su número de afiliado (número entero de 4 dígitos) 
y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). 

Para finalizar se ingresa -1 como número de socio. 

Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.

b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado.
"""

def listado_pacientes():

    lista_urgencia = []
    lista_turno = []
    
    while True:

        num_afiliado = int(input("Ingrese el numero de afiliado (-1 para salir): "))
        
        if num_afiliado == -1:

            break
            
        tipo_atencion = int(input("El paciente entro por urgencia? (0: Si - 1: Por turno): "))

        
        if tipo_atencion == 0:

            lista_urgencia.append(num_afiliado)

        elif tipo_atencion == 1:

            lista_turno.append(num_afiliado)
    
    return lista_urgencia, lista_turno

def mostrar_listados(urgencias, turnos):

    print("\nPacientes atendidos por urgencia.")
    for i, paciente in enumerate(urgencias, 1):

        return f"{i}. Afiliado: {paciente}"
    
    print("\nPacientes atendidos por turno.")
    for i, paciente in enumerate(turnos, 1):

        return f"{i}. Afiliado: {paciente}"

def buscar_afiliado(urgencias, turnos):

    while True:

        num_buscar = int(input("\nIngrese el número de afiliado a buscar (-1 para salir): "))
        
        if num_buscar == -1:
            break
            

        conteo_urgencia = urgencias.count(num_buscar)
        
        conteo_turno = turnos.count(num_buscar)
        
        print(f"\nResultados para afiliado {num_buscar}:")
        print(f"Veces atendido por urgencia: {conteo_urgencia}")
        print(f"Veces atendido por turno: {conteo_turno}")
        print(f"Total de atenciones: {conteo_urgencia + conteo_turno}")

def main():

    print("Ingrese los datos de los pacientes (ingrese -1 para finalizar)")
    
    urgencias, turnos = listado_pacientes()
    
    print(mostrar_listados(urgencias, turnos))
    

    print("\nBusqueda de afiliados.")
    buscar_afiliado(urgencias, turnos)


if __name__ == "__main__":
    main()