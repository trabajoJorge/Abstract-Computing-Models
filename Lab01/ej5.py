print("\n 5. Dados 3 n´umeros guardados en las variables a, b y c (de forma que a y b tengan el mismo n´umero y c sea mayor), programa las instrucciones assert que veriﬁquen que:)")
a= int(input("Introduce a: "))
b= int(input("Introduce b: "))
c= int(input("Introduce c: "))
assert a==b, "a y b son iguales"
assert b<c, "b es menor que c"
assert c>a, "b es menor que c"