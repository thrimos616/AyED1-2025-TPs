jijo = 4

"""
# Matriz a)
matriz1 = [[0 for n in range(jijo)] for n in range(jijo)]

num = 1
for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        if matriz1[i] == matriz1[j]:
            matriz1[i][j] = num
            num += 2

for linea in matriz1:
    print(linea)

"""
"""
# Matriz b)
matriz2 = [[0 for n in range(jijo)] for n in range(jijo)]

num2 = len(matriz2) - 1 

exp = len(matriz2) - 1

for i in range(len(matriz2)):

        for j in range(len(matriz2)):

                if num2 == j:

                        resultado = 3 ** exp
                
                        matriz2[i][j] = resultado

                        num2 -= 1

                        exp -= 1

for linea2 in matriz2:

        print(linea2)"""

# MATRIZ C

matriz3 = [[0 for n in range(jijo)] for n in range(jijo)]

num3 = len(matriz3)

for i in range(len(matriz3)):

        for j in range(len(matriz3)):

                if num3 > matriz3[i][j]:

                        matriz3[i][j] = num3

                num3 = num3 - len(matriz3)



                        
for linea3 in matriz3:

        print(linea3)