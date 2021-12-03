import random
print("11. Inicializa una matriz (lista de listas) de 6 × 3 con valores comprendidos entre -5 y 5.")
def ej11():
    matriz=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j]=random.randint(-5,5)
    return matriz
print(ej11())