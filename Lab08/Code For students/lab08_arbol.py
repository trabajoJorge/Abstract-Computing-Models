

def prim_algorithm(graph):
      # Inicializo las variables
      nodosMarcados= [0]*len(graph)
      arbol= []

      # Creo un arbol de las msimas dimensiones que el grafo
      for i in range(len(graph)):
            c=[float("inf")]*len(graph)
            arbol.append(c)
      # Elijo el nodo 0 para comenzar
      nodosMarcados[0]=1

      while 0 in nodosMarcados:
            infoMenor= getMinInfo(graph, nodosMarcados)
            # menor valor o peso de la arista de menor peso: infoMenor[0]
            # fila de la arista de menor peso: infoMenor[1]
            # columna de la arista de menor peso: infoMenor[2]

            # Asigno el valor minimo a la arista en el arbol
            arbol[infoMenor[1]][infoMenor[2]]=infoMenor[0]
            arbol[infoMenor[2]][infoMenor[1]]=infoMenor[0]

            # Marco ambos nodos, el de inicio y destino
            nodosMarcados[infoMenor[1]]=1
            nodosMarcados[infoMenor[2]]=1

      return arbol

# Funcion auxiliar que busca obtener los valores minimos para elegir el sigiente paso del algoritmo
# prim.
def getMinInfo(graph, nodosMarcados):
      # Inicializo las variables
      minimo= float("inf")
      filaMin= float("inf")
      colMin= float("inf")

      # Recorro el grafo filtrando los nodos marcados, buscando el minimo valor de una arista hacia un
      # nodo no marcado.
      for i in range(len(nodosMarcados)):
            # Fitro los nodos marcados
            if nodosMarcados[i]==1:
                  # Busco la arista de menor peso
                  for j in range(len(nodosMarcados)):
                        if nodosMarcados[j]==0 and graph[i][j]<minimo: 
                              # Recojo la informacion de la arista
                              minimo= graph[i][j]
                              filaMin= i
                              colMin= j
      # La devuelvo en una lista
      return [minimo, filaMin, colMin]



def test():
      
      g1 =  [[float("inf"), 2.0],
            [2.0, float("inf")]]
      
      assert prim_algorithm(g1) == g1
      
      
            
      g2 = [[float("inf"), 5.0, 3.0],
            [5.0, float("inf"), float("inf")],
            [3.0, float("inf"), float("inf")]]
      
      assert prim_algorithm(g2) == g2
            
      
      
      g3 = [[float("inf"), 1.0, 2.0, 3.0, 4.0],
            [1.0, float("inf"), float("inf"), float("inf"), 8.0],
            [2.0, float("inf"), float("inf"), 2.0, 3.0],
            [3.0, float("inf"), 2.0, float("inf"), 5.0],
            [4.0, 8.0, 3.0, 5.0, float("inf")]]
      
      assert prim_algorithm(g3) == [[float("inf"), 1.0, 2.0, float("inf"), float("inf")], 
                                    [1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                    [2.0, float("inf"), float("inf"), 2.0, 3.0], 
                                    [float("inf"), float("inf"), 2.0, float("inf"), float("inf")], 
                                    [float("inf"), float("inf"), 3.0, float("inf"), float("inf")]] 
      
      
            
      g4 = [[float("inf"), 6.0, 2.0, 5.0],
            [6.0, float("inf"), 4.0, float("inf")],
            [2.0, 4.0, float("inf"), 2.0],
            [5.0, float("inf"), 2.0, float("inf")]]
      
      assert prim_algorithm(g4) == [[float("inf"), float("inf"), 2.0, float("inf")], 
                                    [float("inf"), float("inf"), 4.0, float("inf")], 
                                    [2.0, 4.0, float("inf"), 2.0], 
                                    [float("inf"), float("inf"), 2.0, float("inf")]]
      
      
            
      g5 = [[float("inf"), 10.0, 1.0, float("inf"), float("inf"), float("inf")],
            [10.0, float("inf"), float("inf"), 5.0, 4.0, float("inf")],
            [1.0, float("inf"), float("inf"), 8.0, 2.0, 3.0],
            [float("inf"), 5.0, 8.0, float("inf"), float("inf"), 2.0],
            [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")],
            [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
      
      assert prim_algorithm(g5) == [[float("inf"), float("inf"), 1.0, float("inf"), float("inf"), float("inf")], 
                                    [float("inf"), float("inf"),float("inf"), float("inf"), 4.0, float("inf")], 
                                    [1.0, float("inf"), float("inf"), float("inf"), 2.0, 3.0], 
                                    [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2.0], 
                                    [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")], 
                                    [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
      
      
      
      g6 = [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")],
            [3.0, float("inf"), 8.0, 10.0, 5.0, float("inf"), float("inf")],
            [1.0, 8.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
            [float("inf"), 10.0, float("inf"), float("inf"), 6.0, float("inf"), 9.0],
            [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0],
            [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), 4.0],
            [float("inf"),float("inf"),float("inf"), 9.0, 2.0, 4.0, float("inf")]]
      
      
      assert prim_algorithm(g6) == [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                    [3.0, float("inf"), float("inf"), float("inf"), 5.0, float("inf"), float("inf")], 
                                    [1.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")], 
                                    [float("inf"), float("inf"), float("inf"), float("inf"), 6.0, float("inf"), float("inf")], 
                                    [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0], 
                                    [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), float("inf")], 
                                    [float("inf"), float("inf"), float("inf"), float("inf"), 2.0, float("inf"), float("inf")]]


test()
print("Todo correcto")