#import matplotlib
from tools import list_minisat2list_our_sat

from colour_tools import fromAdjacencyToGX ##, visualizeGXGraph

def list2dimacs(my_list):
      return ('\n'.join(' '.join(map(str,sl)) for sl in my_list))


# colores [r, g, b]  ([red, green, blue])
# Cuando el grafo tiene m nodos tu formula tiene 3xm variables.
# Dada la variable i, (i-1)/3 corresponde al nodo del grafo y (i-1)%3 al color  
def reduce_3colorable_to_SAT(graph):
      return createClausesConectionDiferentColor(graph, createClausesUniqueColor(len(graph)))

def createClausesUniqueColor(nVariables):
      result= []
      v1=0
      v2=0
      v3=0
      for v in range (nVariables):
            v1= v3+1
            v2= v1+1
            v3= v2+1
            result.append([v1, v2, v3])
            result.append([-v1, -v2])
            result.append([-v1, -v3])
            result.append([-v2, -v3])
      return result

def createClausesConectionDiferentColor(graph, result):
      for i in range(len(graph)):
            for j in range(i, len(graph[i])):
                  if i!=j and graph[i][j]==1: #Estan conectados
                        v1= 3*i+1
                        v2= 3*j+1
                        result.append([-(v1), -(v2)])
                        result.append([-(v1+1), -(v2+1)])
                        result.append([-(v1+2), -(v2+2)])
      return result

def test():         
      g1 = [[1, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 0],
            [0, 1, 0, 1]]

      g0= [ [1, 1],
            [1, 1]]

      reduce_3colorable_to_SAT(g1)
      f = open("g1.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g1)))
      f.close()
      # SATISFIABLE

      graph = fromAdjacencyToGX(g1)
      print(graph)
      #visualizeGXGraph(graph, "g1.txt")

      
      g2 = [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1]]
      
      f = open("g2.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g2)))
      f.close()
      # SATISFIABLE

      graph = fromAdjacencyToGX(g2)
      print(graph)
      #visualizeGXGraph(graph, "g2.txt")
      

      g3 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
      
      f = open("g3.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g3)))
      f.close()
      # UNSATISFIABLE
      
      graph = fromAdjacencyToGX(g3)
      print(graph)
      #visualizeGXGraph(graph, "g3.txt")


      g4 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
      
      f = open("g4.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g4)))
      f.close()
      # UNSATISFIABLE
      
      graph = fromAdjacencyToGX(g4)
      print(graph)
      #visualizeGXGraph(graph, "g4.txt")


      g5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
      
      f = open("g5.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g5)))
      f.close()
      # UNSATISFIABLE
      
      graph = fromAdjacencyToGX(g5)
      print(graph)
      #visualizeGXGraph(graph, "g5.txt")

      g6 = [[1, 1, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1]]
      
      f = open("g6.txt", "w")
      f.write(list2dimacs(reduce_3colorable_to_SAT(g6)))
      f.close()
      # SATISFIABLE
      
      graph = fromAdjacencyToGX(g6)
      print(graph)
      #visualizeGXGraph(graph, "g6.txt")

test()
print("Proceso finalizado")