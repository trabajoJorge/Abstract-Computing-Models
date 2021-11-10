from vertex_cover import solve_vc

def matrizComplementaria(matriz):
    for i in range(len(matriz)):
        if (matriz[i]==0): 
            matriz[i]=1
        else: 
            matriz[i]=0
    return matriz

def multisolve(graph, problem):  
    # Caso base: se aplica la funcion y se devuelve el resultado
    if problem== "VERTEX COVER": 
        return solve_vc(graph) 
    # Se aplica la función y de el resultado se hace la matriz complementaría
    elif problem == "INDEPENDENT SET": 
        return matrizComplementaria(solve_vc(graph)) 
    # Se aplica la funcion complementaria excepto en la diagonal principal y despues se aplica la funcion  
    elif problem == "CLIQUE": 
        result=[]
        for i in range(len(graph)):
            result.append([])
            for j in range(len(graph[i])):
                if(graph[i][j] == 0 and i != j):
                    result[i].append(1)
                else:
                    result[i].append(0)
        return matrizComplementaria(solve_vc(result))
    return []

def test():
    graph = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
    
    sol_vertex = multisolve(graph, "VERTEX COVER")
    sol_clique = multisolve(graph, "CLIQUE")
    sol_independent_set =  multisolve(graph, "INDEPENDENT SET")

    assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
    assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
    assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]

    graph = [[0,1,1],[1,0,1],[1,1,0]]
    
    sol_vertex = multisolve(graph, "VERTEX COVER")
    sol_clique = multisolve(graph, "CLIQUE")
    sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
        
    assert sol_vertex in [[0,1,1], [1,0,1], [1,1,0]]
    assert sol_independent_set in [[1,0,0],[0,1,0],[0,0,1]]
    assert sol_clique in [[1,1,1]]
    

test()
print("Todo correcto")