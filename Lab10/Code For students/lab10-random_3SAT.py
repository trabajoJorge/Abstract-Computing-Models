import math
from random import choice
from random import randrange
from lab07_pre_processing import sat_preprocessing
from Lab09_sat_solver import solve_SAT


def procesado_Clausula(clause, assigment):
    for literal in clause:
        if abs(literal)>0 and assigment[abs(literal)]==1:
            return True;
        elif abs(literal)<0 and assigment[abs(literal)]==0:
            return True
    return False

def isSatisfactible(clausulas, asig):
    entra=0
    for clausula in clausulas:
        entra=0
        for literal in clausula:
            if literal>0 and asig[abs(literal)]==1: 
                entra= 1
                break
            elif literal<0 and asig[abs(literal)]==0: 
                entra= 1
                break
        if entra==0: 
            return False
    return True

def sigLit(lastElection):
    if lastElection==-1: return randrange(3)
    elif lastElection==2: return randrange(2)
    elif lastElection==1: 
        r=randrange(2)
        if r==1: return 2
        else: return 0
    else: #lastElection==0
        r=randrange(2)
        if r==1: return 1
        else: return 2

def random_3SAT (clauses, num_variables):
    print("_____________________________________________________________________________________")
    vueltas= 10/((2/3)**num_variables)
    vueltas= math.ceil(vueltas) #Para truncar
    print("Vueltas: ", vueltas)
    assignment = [None] + [choice([0,1]) for n in range(num_variables)]
    lastElecction=-1

    for i in range(vueltas):
        for j in range(1, num_variables+1):
            if not procesado_Clausula(clauses[i], assignment): 
                lastElecction= sigLit(lastElecction)
                if assignment[abs(clauses[i][lastElecction])]==0: assignment[abs(clauses[i][lastElecction])]=1
                else: assignment[abs(clauses[i][lastElecction])]=0
            if isSatisfactible(clauses, assignment): return "SAT"
    
    assert not isSatisfactible(clauses, assignment);
    return "UNSAT"



def test():
    aciertos=0
    fallos=0

    clauses = [[1, -2, -4], [1, 4, 2], [2, -1, -4], [2, 4, -1], [-3, -1, 4], [-3, 1, -2], [-3, -4, 2]]
    r= random_3SAT(clauses, 4)
    print("Esta instancia es SAT. El algoritmo random devuelve: ", r)
    if r=="SAT": aciertos+=1
    else: fallos+=1
    
    clauses = [ [3, 1, 2], [1, 2, -3],[-3, 1, -2], [1, 3, -2],
                [3, -1, 2], [-1, 2, -3],[-3, -1, -2], [-1, 4, -2]]
    r=random_3SAT(clauses, 4) 
    print("Esta instancia es SAT. El algoritmo random devuelve: ", r)
    if r=="SAT": aciertos+=1
    else: fallos+=1

    clauses = [ [-2, -3, -1], [3, -2, 1], [-3, 2, 1],
                [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    r=random_3SAT(clauses, 3) 
    print("Esta instancia es SAT. El algoritmo random devuelve: ", r)
    if r=="SAT": aciertos+=1
    else: fallos+=1
    
    clauses = [ [1, -2, -3], [2, -3, 1], [3, -2, 1],
                [2, 3, 1]]
    r=random_3SAT(clauses, 3) 
    print("Esta instancia es SAT. El algoritmo random devuelve: ", r)
    if r=="SAT": aciertos+=1
    else: fallos+=1
    
    clauses = [ [2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
                [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
                [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
                [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
                [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    r=random_3SAT(clauses, 3)
    print("Esta instancia es UNSAT. El algoritmo random devuelve: ", r)
    assert r=="UNSAT"
    if r=="UNSAT": aciertos+=1
    else: fallos+=1

    print("Esta ejecucion ha fallado: ", fallos, " veces.")
    print("Esta ejecucion ha acertado: ", aciertos, " veces.")

test()    
