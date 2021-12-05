from __future__ import division

#import matplotlib
from tools import list_minisat2list_our_sat

#Graph Visualization
#import matplotlib.pyplot as plt
#import networkx as nx
#from networkx.readwrite import json_graph
import json
    
def my_colour(last_line, node):
    last_line=last_line[:-2] #Remove ' 0'
    last_line=last_line.split(None, 3*node)
    my_numbers=last_line[-1].split(" ", 3)
    if int(my_numbers[0])>0:
        return 0
    elif int(my_numbers[1])>0:
        return 1
    elif int(my_numbers[2])>0:
        return 2
    else:
        return -1 #ERROR, 3-coloreable should return at least one True - 1 (if satisfiable)
    
#Graph Visualization
def visualizeGXGraph(graph, file_name):
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    G = nx.Graph()
    # add nodes
    for node in nodes:
        G.add_node(node)    
    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])
    
    patata = list_minisat2list_our_sat(file_name)
    print(patata)
    
    import os
    my_command = 'minisat ' + file_name + ' ' + file_name + '_output.txt'
    p = os.popen(my_command,"r")
    while 1:
        line = p.readline()
        if not line: break
        print(line)
    
    output_file = file_name + '_output.txt'
    f_read = open(output_file, "r")
    last_line = f_read.readlines()[-1]
    print(last_line)
    f_read.close()
    
    if "UNSAT" in last_line:
        print("NOT SATISFIABLE -> CANNOT GRAPHICALLY REPRESENT GRAPH")
    else:
        print("DISPLAYING GRAPH FOR: " + file_name)
        color_map = []
        for node in G:        
            #colour = node
            colour = my_colour(last_line, node) #0: red, 1: green, 2: blue
            if colour==0:
                color_map.append('red')
            elif colour==1:
                color_map.append('green')
            else: #colour==2
                color_map.append('blue')      
        nx.draw(G, node_color = color_map, with_labels = True)
    
        plt.show()
        
        #To JSON
        #print json.dumps(json_graph.node_link_data(G))        
        f_json = open(file_name + '_json.txt', "w")
        f_json.write(json.dumps(json_graph.node_link_data(G)))
        f_json.close()
    

#From adjacency matrix to GX graph, plot included
def fromAdjacencyToGX(graph):
    GX_nodes = []
    for i in range(0, len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j]==1:
                GX_nodes.append([i, j])
                
    return GX_nodes
