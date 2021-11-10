print("\n 10. Imprime en la pantalla el n´umero de iteraciones necesario para reducir a 1todos los n´umeros de una lista de n´umeros dada. Para reducir un n´umero, n, 1, si n es par se debe dividir entre 2, mientras que si n es impar se debe multiplicar por 3 y al resultado sumarle 1 (ver https://en.wikipedia.org/wiki/Collatz_conjecture). Se debe imprimir una lista en la que aparezcan el numero de iteraciones necesarios para reducir a 1 cada uno de los numeros de la lista original. Por ejemplo, si la lista original es [6, 11, 27, 32, 33] el resultado debe ser [8, 14, 111, 5, 26].")
a= [6, 11, 27, 32, 33]
b= []
for i in range (0, len(a)):
    b.append(0)

for i in range (0, len(a)):
    count=0
    num=a[i]
    while(num != 1 ):
        if (num%2==0):
            num=num/2
        else:
            num=3*num+1
        count=count+1
    b[i]= count
print (b)