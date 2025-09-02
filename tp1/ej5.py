"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. 
Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.

b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4
"""

# a 

num1 = int(input("Introduzca un numero: "))

oblongo = lambda x:x * (x + 1)

print(oblongo(num1))

# b

num2 = int(input("Introduzca un numero: "))

triangular = lambda x:(x * (x + 1)) // 2

print(triangular(num2))