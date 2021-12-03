print("\n 9. Inicializa una lista en Python en la que haya al menos 3 apariciones del numero 4. Sustituir todas las apariciones del n´umero 4 por 10.")
a= [1, 4, 4, 4, 4]
for i in range(0, len(a)):
    if (a[i]==4):
        a[i]=10
print(a)       