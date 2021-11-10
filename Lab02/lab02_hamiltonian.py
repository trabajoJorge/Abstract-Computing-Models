from itertools import permutations

def permutar(xs):
    if len(xs) <= 1:
        yield xs
    else:
        for i in range(len(xs)):
            for p in permutar(xs[:i] + xs[i + 1:]):
                yield [xs[i]] + p



def graph_has_Hamiltonian_circuit(g):
    camino=[]                                               # Para guardar todos los caminos posibles
    for i in range(0,len(g)):                               # Creo un array del tipo [1,2,3...n] siendo n el numero de nodos 
        camino.append(i+1)
    posibles_caminos= permutations(camino, len(camino))     # Por cada elemento del array saco sus permutaciones y creo un array de arrays o matriz
    for i in posibles_caminos:                              # Recorro uno a uno todos las posibilidades de caminos obtneidas anteriormente
        nodos_conectados = 0                       
        for j in range(0,len(i)-1):                         # Recorro una posibilidad de camino  
            if (g [i[j]-1] [i[j+1]-1] ==1):                 # Compruebo si en la matriz hay algun uno, es decir, si estan conectados
                nodos_conectados=nodos_conectados+1         # Cuento cada conexion de nodos para comprobar se cumple
            else:
                break
        if(g[i[len(i)-1]-1][i[0]-1]==1):                    # Compruebo si el nodo inicial y el final son iguales
            nodos_conectados=nodos_conectados+1             # Cuento esa conexión
        if(nodos_conectados==len(i)):                       # Compruebo si el numero de conexiones es igual a la cantidad de nodos del grafo
                                                            # de ser así, existe un circuito hamiltoniano
            print(i)                                        # Por ello lo imprimo
            return True                                     # En cuanto se encuentra el primero, se devuelve y se corta la ejecucion
    return False

    # El tiempo de ejecucion del algoritmo es del O(2^n)

def test():
    g1 = [[1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g3)
    
    g4 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    g5 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g5)
    
    g6 = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g6)
    
    g7 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
     
    
    assert not graph_has_Hamiltonian_circuit(g7)    
    
    print ("Supera todos los test")

test()

