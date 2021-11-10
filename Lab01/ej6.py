print("\n 6. Calcula la distancia euclıdea entre dos puntos. Las coordenadas de cada punto se dan como entrada. Dados dos puntos (x1,y1),(x2,y2), la distancia entre dichos puntos se deﬁne como:")
import math
print ("Introduce el primer punto x e y: ")
x1, y1 = int(input("Introduce x: ")), int(input("Introduce y: "))
print ("Introduce el segundo punto x e y: ")
x2, y2 = int(input("Introduce x: ")), int(input("Introduce y: "))
print (math.sqrt( (x2 - x1)*2 + (y2 - y1)*2 ))