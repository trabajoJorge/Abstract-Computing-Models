from time import time
from tools import list_minisat2list_our_sat
from lab07_pre_processing import sat_preprocessing
    
	
def solve_SAT(num_variables, clausulas):
    asig = [None] * ( num_variables+1 )
    asig[0] = 0

    sol= solve_SAT_Recursivo(clausulas, asig)
    
    # Asigno a false los valores que no he necesitado asignar
    sol= [0 if value==None else value for value in sol]

    return sol

def solve_SAT_Recursivo(clausulas, asig):
    clausulas, asig = sat_preprocessing(len(asig), clausulas, asig)
    if clausulas==[]: return asig
    elif clausulas==[[1],[-1]]: return "UNSATISFIABLE"
    else:
        var= abs(clausulas[0][0])
        asig1= asig.copy()
        clausulas1= clausulas.copy()
        asig1[var]=1
        result= solve_SAT_Recursivo(clausulas1, asig1)
        if result!="UNSATISFIABLE": 
            return result
        else:
            asig[var]=0
            return solve_SAT_Recursivo(clausulas, asig)

    
def test():
    clausulas = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    solutions = [[0, 0, 0, 0],
                 [0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0],
                 [None, 0, 0, 0],
                 [None, 0, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 1, 0]]
    
    assert solve_SAT(3,clausulas) in solutions
    
    
    clausulas = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    solutions = [[0, 1, 0, 0], 
                 [0, 1, 0, 1], 
                 [0, 1, 1, 0], 
                 [0, 1, 1, 1], 
                 [1, 1, 0, 0], 
                 [1, 1, 0, 1], 
                 [1, 1, 1, 0], 
                 [1, 1, 1, 1],
                 [None, 1, 0, 0], 
                 [None, 1, 0, 1], 
                 [None, 1, 1, 0], 
                 [None, 1, 1, 1],
                 [None, 1, None, None]]

    assert solve_SAT(3,clausulas) in solutions
    

    clausulas = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    print (solve_SAT(3,clausulas))
    assert solve_SAT(3,clausulas) == ['U', 'N', 'S', 'A', 'T', 'I', 'S', 'F', 'I', 'A', 'B', 'L', 'E']    
     
    clausulas = [[4, -18, 19],[3, 18, -5],[-5, -8, -15],[-20, 7, -16],[10, -13, -7],
               [-12, -9, 17],[17, 19, 5],[-16, 9, 15], [11, -5, -14],[18, -10, 13],
               [-3, 11, 12],[-6, -17, -8],[-18, 14, 1],[-19, -15, 10],[12, 18, -19],
               [-8, 4, 7],[-8, -9, 4],[7, 17, -15],[12, -7, -14],[-10, -11, 8],
               [2, -15, -11],[9, 6, 1],[-11, 20, -17],[9, -15, 13],[12, -7, -17],
               [-18, -2, 20],[20, 12, 4],[19, 11, 14],[-16, 18, -4],[-1, -17, -19],
               [-13, 15, 10],[-12, -14, -13],[12, -14, -7],[-7, 16, 10],[6, 10, 7],
               [20, 14, -16],[-19, 17, 11],[-7, 1, -20],[-5, 12, 15],[-4, -9, -13],
               [12, -11, -7],[-5, 19, -8],[-16],[20, -14, -15],[13, -4, 10],
               [14, 7, 10],[-5, 9, 20],[10, 1, -19],[-16, -15, -1],[16, 3, -11],
               [-15, -10, 4],[4, -15, -3],[-10, -16, 11],[-8, 12, -5],[14, -6, 12],
               [1, 6, 11],[-13, -5, -1],[-12],[1, -20, 19],[-2, -13, -8],
               [18],[-11, 14, 9],[-6, -15, -2],[-5],[-6, 17, 5],
               [-13, 5, -19],[20, -1, 14],[9, -17, 15],[-5, 19, -18],[-12, 8, -10],
               [-18, 14, -4],[15, -9, 13],[9, -5, -1],[10, -19, -14],[20, 9, 4],
               [-9, -2, 19],[-5, 13, -17],[2, -10, -18],[-18, 3, 11],[7, -9, 17],
               [-15, -6, -3],[-2, 3, -13],[12, 3, -2],[2, -2, -3, 17],[20, -15, -16],
               [-5, -17, -19],[-20, -18, 11],[-9, 1, -5],[-19, 9, 17],[17],[1],
               [4, -16, -5]]
    assert solve_SAT(20, clausulas) == ['U', 'N', 'S', 'A', 'T', 'I', 'S', 'F', 'I', 'A', 'B', 'L', 'E']
    
    print("Tests passed") 
   
    clauses = [[-6, -4, -2, 6], [-5], [7], [1, -3], 
               [1, -4, -1, -7], [-6, -1], [1], [-7]]
    
    assert solve_SAT(7, clauses) == ['U', 'N', 'S', 'A', 'T', 'I', 'S', 'F', 'I', 'A', 'B', 'L', 'E']

    # Para probar el juego de pruebas
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/1-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("1 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (1): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/2-sat.cnf')
    total_elapsed_time = time() - start_time   
    print("2 sat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (2): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/3-sat.cnf')
    total_elapsed_time = time() - start_time   
    print("3 sat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (3): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/4-sat.cnf')
    total_elapsed_time = time() - start_time   
    print("4 sat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (4): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/5-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("5 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (5): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/6-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("6 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (6): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/7-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("7 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (7): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/8-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("8 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (8): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/9-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("9 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (9): %0.10f seconds.\n" % total_elapsed_time)
    
    start_time = time()
    tupla = list_minisat2list_our_sat ('instancias/10-unsat.cnf')
    total_elapsed_time = time() - start_time   
    print("10 unsat: " , solve_SAT(tupla[0], tupla[1]))
    print("Elapsed time (10): %0.10f seconds.\n" % total_elapsed_time)


start_time = time()
test()
elapsed_time = time() - start_time   
print("Elapsed time: %0.10f seconds." % elapsed_time) 