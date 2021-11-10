
##  EJERCICIO 1 ##
print("\n 1. Calcular el valor absoluto de un numero negativo dado como entrada.")
print(abs(int(input("Enter your value: "))))

##  EJERCICIO 2 ##
print("\n 2. Suma dos numeros enteros (los dos n´umeros se proporcionan como entrada).")
print(int(input("Enter value 1: ")) +int(input("Enter value 2: ")))

##  EJERCICIO 3 ##
print("\n 3. Convierte la temperatura de grados Celsius (tCelsius como valor de entrada) a grados Fahrenheit:")
print( str(round( 9/5*(int(input("Introduce los grados celsius:"))+32), 2)) + " grados Fahrenheit")

##  EJERCICIO 4 ##
print("\n 4. Calcula el área de una esfera (radio como entrada):")
import math ##Lo importo para poder utilizar la funcion de pi
print (4*math.pi*(int(input("Introduce el radio de la esfera: ")))**2) ## Ejecuto la función y la imprimo

##  EJERCICIO 5 ##
print("\n 5. Dados 3 n´umeros guardados en las variables a, b y c (de forma que a y b tengan el mismo n´umero y c sea mayor), programa las instrucciones assert que veriﬁquen que:)")
a, b, c= int(input("Introduce a: ")), int(input("Introduce b: ")),  int(input("Introduce c: "))
assert a==b, "a y b son iguales"
assert b<c, "b es menor que c"
assert c>a, "b es menor que c"

##  EJERCICIO 6 ##
print("\n 6. Calcula la distancia euclıdea entre dos puntos. Las coordenadas de cada punto se dan como entrada. Dados dos puntos (x1,y1),(x2,y2), la distancia entre dichos puntos se deﬁne como:")
import math
print ("Introduce el primer punto x e y: ")
x1, y1 = int(input("Introduce x: ")), int(input("Introduce y: ")) ## Pido el input mediante un mensaje y lo almaceno en las variables
print ("Introduce el segundo punto x e y: ")
x2, y2 = int(input("Introduce x: ")), int(input("Introduce y: "))
print (math.sqrt( (x2 - x1)*2 + (y2 - y1)*2 )) ## Ejecuto la función y la imprimo

##  EJERCICIO 7 ##
print("\n 7.Calcula la siguiente expresi´on (x, y son datos de entrada):")
import math
print ("Introduce el punto x e y: ")
x, y = int(input("Introduce x: ")), int(input("Introduce y: "))
print ( 5*x*3+ math.sqrt(x**2+y**2)+math.e*math.log(x) ) ## Ejecuto la función y la imprimo

##  EJERCICIO 8 ##
print("\n 8. Inicializa una coleccion de datos en Python que tenga los siguientes valores: 1, 2, 3, 4, 5 Usa los operadores corchete ([, ]) para indicar el inicio y el ﬁnal de los elementos de la coleccion.")
a= [1, 2, 3, 4, 5]
print(a)
print(type(a))

##  EJERCICIO 9 ##
print("\n 9. Inicializa una lista en Python en la que haya al menos 3 apariciones del numero 4. Sustituir todas las apariciones del n´umero 4 por 10.")
a= [1, 4, 4, 4, 4]
for i in range(0, len(a)):
    if (a[i]==4):
        a[i]=10
print(a)   

##  EJERCICIO 10 ##
print("\n 10. Imprime en la pantalla el n´umero de iteraciones necesario para reducir a 1todos los n´umeros de una lista de n´umeros dada. Para reducir un n´umero, n, 1, si n es par se debe dividir entre 2, mientras que si n es impar se debe multiplicar por 3 y al resultado sumarle 1 (ver https://en.wikipedia.org/wiki/Collatz_conjecture). Se debe imprimir una lista en la que aparezcan el numero de iteraciones necesarios para reducir a 1 cada uno de los numeros de la lista original. Por ejemplo, si la lista original es [6, 11, 27, 32, 33] el resultado debe ser [8, 14, 111, 5, 26].")
a= [6, 11, 27, 32, 33]
b= []
for i in range (0, len(a)):
    b.append(0)

for i in range (0, len(a)): #recorro la lista
    count=0
    num=a[i]
    while(num != 1 ):
        if (num%2==0): #Numero par
            num=num/2
        else:
            num=3*num+1  #Numero impar
        count=count+1
    b[i]= count
print (b)

##  EJERCICIO 11 ##
import random
print("\n 11. Inicializa una matriz (lista de listas) de 6 × 3 con valores comprendidos entre -5 y 5.")
# Funcion para inicializar una matrix de 6x3 con valores comprendidos entre -5 y 5. Se define como funcion 
# debido que se reutiliza posteriormente
def ej11():
    matriz=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j]=random.randint(-5,5)
    return matriz
print(ej11()) #Ejecuto la función

##  EJERCICIO 12 ##
print("\n 12. Crea un m´etodo en Python que, dada una matriz cualquiera y un n´umero x, devuelva el n´umero de veces que x aparece en dicha matriz.")
def ej12(matriz, num):
    count=0
    #Se recorre la matriz
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if (matriz[i][j]==num):
                count = count +1 # Se le suma 1 a count por cada aparicion
    return count
         
matriz=ej11() # Uso la funcion anterior para crear la matriz y darle valores
print(ej11)
n=random.randint(-5,5) # Se coge una numero al azar entre -5 y 5
print(ej12(matriz, n)) # Se ejecuta la funcion anterior para ver cuantas aparicione tiene ese numero

##  EJERCICIO 13 ##
print("\n 13. Crea un m´etodo en Python que devuelva si hay alg´un número entre 4 y 7 en una matriz (lista de listas) de núumeros.")
count=0
matriz= ej11()
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        if (matriz[i][j]<=7 and matriz[i][j]>=4): #Compruebo si el valor esta ente 4 y 7
            count = count +1
if count !=0: #Al acabar el conteo hay algun numero entre 4 y 7
    print("Hay "+str(count)+" numeros enteros entre 4 y 7") 

else: #Al acabar el conteo no hay ningun numero entre 4 y 7
    print("No hay algun numero entero entre 4 y 7")

##  EJERCICIO 14 ##
print("\n 14. Dadas una lista de números enteros (positivos o negativos) y una lista de booleanos (True, False) con el mismo tamaño, crea una función que devuelva el número de veces que un número positivo es True y uno negativo es False en su correspondiente posici´on. Por ejemplo, dados: a = [-2, 3, 4, -7, 10, -234] y b = [True, True, True, True, False, False], se debe devolver: (2, 1)")

li=[-2, 3, 4, -7, 10, -234]
lb=[True, True, True, True, False, False]
ct=0
cf=0

for i in range(0, len(li)):
    if (li[i]>=0 and lb[i]==True): ct = ct +1 #Cuando la celda de ambas es positiva y true sumo 1 a ct
    if (li[i]<0 and lb[i]==False): cf = cf +1 #Cuando la celda de ambas es negativa y false sumo 1 a cf
print("("+str(ct)+", "+str(cf)+")")


