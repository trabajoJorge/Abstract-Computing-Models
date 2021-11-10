
from time import time
from math import inf

def sigiente(list, visitados):
      print("***********************************************************")
      print (list)
      print(visitados)
      min= inf
      pos= -1
      for i in range(len(list)):
            print ("Entra FOR")
            if list[i]<min and not visitados[i] and list[i]!=0.0:
                  print ("Entra IF")
                  min= list[i]
                  pos= i
                  print ("MIN: ", min)
                  print ("POS: ", pos)
      return pos

# algoritmo voraz de Dijkstra
def Dijkstra (graph, initial):
      
      sol= []
      visitados=[]
      grafo= graph
      for i in range(len(grafo)):
            sol.append(inf)
            visitados.append(False)
      sol[initial]=0.0
      coste= 0
      visitados[initial]=True


      actualNode = graph[initial]
      sigFila= initial
      for cout in range(len(graph)):
            sigCol= sigiente(actualNode, visitados)
            if sigCol==-1: break
            siguiente= actualNode[sigCol]
            print("Siguiente: ", siguiente)
            visitados[sigCol]=True
            coste= coste+siguiente
            sol[sigCol]=coste
            actualNode= graph[sigCol]
      print (sol)
      return sol



def test():
      
      g0 =  [[0.0, 5.0, 1.0, inf],
            [5.0, 0.0, 1.0, 2.0],
            [1.0, 1.0, 0.0, 10.0],
            [inf, 2.0, 10.0, 0.0]]
      Dijkstra(g0, 3)
      assert Dijkstra(g0, 3) == [4.0, 2.0, 3.0, 0.0]
      
      g1 =  [[0.0, 2.0],
            [2.0, 0.0]]
      
      assert Dijkstra(g1,0) == [0.0,2.0]

      
      
      g2 = [[0.0, 5.0, 3.0],
            [5.0, 0.0, inf],
            [3.0, inf, 0.0]]
      Dijkstra(g2, 1)
      assert Dijkstra(g2, 1) == [5.0, 0.0, 8.0]
      
      '''
      g3 = [[0.0, 1.0, 2.0, 3.0, 4.0],
            [1.0, 0.0, inf, inf, 8.0],
            [2.0, inf, 0.0, 2.0, 2.0],
            [3.0, inf, 2.0, 0.0, 5.0],
            [4.0, 8.0, 2.0, 5.0, 0.0]]
      
      assert Dijkstra(g3, 3) == [3.0, 4.0, 2.0, 0.0, 4.0]
      
      g4 = [[0.0, 6.0, 2.0, 5.0],
            [6.0, 0.0, 4.0, inf],
            [2.0, 4.0, 0.0, 2.0],
            [5.0, inf, 2.0, 0.0]]
      
      assert Dijkstra(g4, 3) == [4.0, 6.0, 2.0, 0.0]
      
      g5 = [[0.0, 10.0, 1.0, inf, inf, inf],
            [10.0, 0.0, inf, 5.0, 4.0, inf],
            [1.0, inf, 0.0, 8.0, 2.0, 3.0],
            [inf, 5.0, 8.0, 0.0, inf, 2.0],
            [inf, 4.0, 2.0, inf, 0.0, inf],
            [inf, inf, 3.0, 2.0, inf, 0.0]]
      
      assert Dijkstra(g5, 0) == [0.0, 7.0, 1.0, 6.0, 3.0, 4.0]
      
      g6 = [[0.0, 3.0, 1.0, inf, inf, inf, inf],
            [3.0, 0.0, 8.0, 10.0, 5.0, inf, inf],
            [1.0, 8.0, 0.0, inf, inf, inf, inf],
            [inf, 10.0, inf, 0.0, 6.0, inf, 9.0],
            [inf, 5.0, inf, 6.0, 0.0, 1.0, 2.0],
            [inf, inf, inf, inf, 1.0, 0.0, 4.0],
            [inf,inf,inf, 9.0, 2.0, 4.0, 0.0]]
      
      assert Dijkstra(g6, 3)  == [13.0, 10.0, 14.0, 0.0, 6.0, 7.0, 8.0]
      '''
start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time)       
print("Todo correcto")