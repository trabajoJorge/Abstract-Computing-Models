from time import time

def partial_validity_check(cover, graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
                if(graph[i][j] == 1):
                    if(cover[i] == 0 and cover[j] == 0 and i!=j):
                            return False
    return True

## vertex_cover_tree inicializa y llama al arbol de busqueda
def vertex_cover_tree(graph):
    n = len(graph)
    cover = [None]*n
    return recursive_vertex_cover(graph, cover)

def recursive_vertex_cover(graph, cover):

    ############
    # TODO: Programa esta parte de la funcion
    #
    # Comprueba es posible construir un cover valido.
    # Si no es posible, devuelve [1]*len(cover).
    # En otro caso, encuentra dos nodos u y v conectados y que no estan en el cover.
    # Si no los hay, completa el cover decidiendo si los que faltan deben formar parte 
    # del cover o no y una vez hecho esto, devuelve el cover completo.
    # En otro caso continua con u y v
    
    if not partial_validity_check(cover, graph): return [1]*len(cover)
    else:
        v=0
        while(v < len(cover) and cover[v] != None): v+=1
        if(v == len(cover)):
            return cover
        else:
            u = v + 1
            if(u >= len(cover)):
                u = v        
    # Final de tu codigo
    # Lo siguiente abre las tres ramas del arbol de busqueda.
    # No modificar nada.
    ##############
    copy_cover = list(cover)
    cover[u] = 1
    cover[v] = 0
    c10 = recursive_vertex_cover(graph, cover)
    cover = list(copy_cover)
    cover[u] = 0
    cover[v] = 1
    c01 = recursive_vertex_cover(graph, cover)
    cover = list(copy_cover)
    cover[u] = 1
    cover[v] = 1
    c11 = recursive_vertex_cover(graph, cover)
    if c10.count(1) <= min(c01.count(1), c11.count(1)):
        return c10
    elif c01.count(1) <= c11.count(1):
        return c01
    else:
        return c11
    
def test():
    
    g1 =  [[1, 1],
           [1, 1]]
       
    g2 = [[1, 1, 1],
          [1, 1, 0],
          [1, 0, 1]]
        
    
    g3 = [[1, 1, 1, 1, 1],
          [1, 1, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1]]
    
        
    g4 = [[1, 1, 1, 1],
          [1, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 0, 1, 1]]
    
       
    g5 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]
    
    g6 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
    
    g7 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]]

    
   
    
##  Descomentar para probar la funcion partial_validity_check
    assert not partial_validity_check([0,0], g1)
    assert not partial_validity_check([0,0,1], g2)
    assert partial_validity_check([1,None,None], g2) 
    assert partial_validity_check([0,None,None], g2) 
    assert partial_validity_check([1,0,0], g2) 
    assert partial_validity_check([1,1,0], g2) 
    assert partial_validity_check([0,1,None], g2)
    assert not partial_validity_check([0,None,0], g2) 
    assert not partial_validity_check([0, 1, 1, 0, 1, 0], g5)
    assert partial_validity_check([0, 1, 1, 1, 0, 0], g5) 
    assert partial_validity_check([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1], g6)
###################################################################  
    
 
#    Descomentar para probar la funcion recursive_vertex_cover
    assert vertex_cover_tree(g1) in [[1,0],[0,1]]
    assert vertex_cover_tree(g2)  == [1,0,0]
    assert vertex_cover_tree(g3) in [[1, 0, 1, 0, 1], 
                                     [1, 0, 0, 1, 1]]
    assert vertex_cover_tree(g4)  == [1, 0, 1, 0]
    assert vertex_cover_tree(g5)  in  [[0, 1, 1, 1, 0, 0], 
                                       [0, 1, 1, 0, 0, 1]]
    assert vertex_cover_tree(g6) in [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
                                     [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
                                     [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]]


start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)      
