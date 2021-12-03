print("14. Dadas una lista de n´umeros enteros (positivos o negativos) y una lista de booleanos (True, False) con el mismo tamaño, crea una función que devuelva el número de veces que un número positivo es True y uno negativo es False en su correspondiente posici´on. Por ejemplo, dados: a = [-2, 3, 4, -7, 10, -234] y b = [True, True, True, True, False, False], se debe devolver: (2, 1)")

li=[-2, 3, 4, -7, 10, -234]
lb=[True, True, True, True, False, False]
ct=0
cf=0

for i in range(0, len(li)):
    if (li[i]>=0 and lb[i]==True): ct = ct +1
    if (li[i]<0 and lb[i]==False): cf = cf +1
print("("+str(ct)+", "+str(cf)+")")