from ej11 import ej11
import random

print("12. Crea un m´etodo en Python que, dada una matriz cualquiera y un n´umero x, devuelva el n´umero de veces que x aparece en dicha matriz.")


def ej12(matriz, num):
    count=0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if (matriz[i][j]==num):
                count = count +1
    return count
         
matriz=ej11()
print(ej11)
n=random.randint(-5,5)
print(ej12(matriz, n))