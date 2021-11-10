
def graph_has_Eulerian_circuit(g):
    cont = 0;                           # Creo un contador incializado a 0 para posteriormente comprobar que todas las aristas de los nodos son pares.
    for i in range(0,len(g)):           # Recorro todos los nodos del grafo.
        for j in range(0,len(g[i])):    # Recorro todas las posiciones de la matriz de abyacencia.
            if(g[i][j] == 1):           # Compruebo con que nodos esta conectado.
                cont+=1;                # Cuento los nodos.
        if(cont % 2 != 0):              # Compruebo que el numero de conexiones del nodo es par, si es asi compruebo el siguiente.
            return False                # De no ser así devuelvo False ya que al ser impar ya no seria eueriano.
    return True                         # Cuando se llega a este punto del metodo podemos dedudcir que todos los nodos tienen un numero de conexiones 
                                        # para y por ende es un grafo euleriano.

    # El tiempo de ejecucion del algoritmo es del O(n^2)
     
def test():
    g1 = [[0, 1, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 1, 0, 1],
          [0, 1, 1, 1, 0]]
    assert not graph_has_Eulerian_circuit(g1)


    g2 = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g2)

    g3 = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1],
          [0, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 0, 1, 1],
          [0, 1, 1, 0, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 0]]
    
    assert not graph_has_Eulerian_circuit(g3)
    
    g4 = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
    
    assert graph_has_Eulerian_circuit(g4)
    
    print ("Supera todos los test")

test()

