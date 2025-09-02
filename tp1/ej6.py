"""
Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. 
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. 
No se permite utilizar facilidades de Python no vistas en clase
"""

def concatenar_enteros(a: int, b: int) -> int:

    return (a * 10**len(str(b))) + b

print(concatenar_enteros(1234, 567))