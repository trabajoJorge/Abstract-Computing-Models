from ej11 import ej11

print("13. Crea un m´etodo en Python que devuelva si hay alg´un número entre 4 y 7 en una matriz (lista de listas) de núumeros.")
count=0
matriz= ej11()
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        if (matriz[i][j]<=7 and matriz[i][j]>=4):
            count = count +1
if count !=0: 
    print("Hay "+str(count)+" numeros enteros entre 4 y 7")

else:
    print("No hay algun numero entero entre 4 y 7")
