print("\n 7.Calcula la siguiente expresi´on (x, y son datos de entrada):")
import math
print ("Introduce el punto x e y: ")
x, y = int(input("Introduce x: ")), int(input("Introduce y: "))
print ( 5*x*3+ math.sqrt(x**2+y**2)+math.e*math.log(x) )