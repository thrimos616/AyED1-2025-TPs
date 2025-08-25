lista = [1, 2, 3]

print(id(lista))      # Ejemplo: 139909752105600
lista.append(4)

print(lista)          # [1, 2, 3, 4]
print(id(lista))      # Mismo id → fue modificado en el lugar
