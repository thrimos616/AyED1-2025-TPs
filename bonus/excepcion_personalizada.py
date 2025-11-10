class DivNumeroNegativo(Exception):
    """Division por numero negativo."""
    pass

def dividir(a, b):
    if b < 0:

        raise DivNumeroNegativo("No se puede dividir con un numero negativo")

    return a / b

try:
    resultado = dividir(10, -2)
    print(resultado)

except DivNumeroNegativo as e:
    
    print(f"ERORR: {e}")
