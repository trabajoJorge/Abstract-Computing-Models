def sat_preprocessing(num_literals, clauses, assignment):
    update = True
    while update:
        update = False 

        # Lista en la que guardo las clausulas a eliminar
        clausulasParaEliminar=[]

        #Etapa A: Variables con clausula unica 
        for clause in clauses:
            # Miramos que clausulas tienen un unico literal
            if len(clause)==1: 
                # Si el literal no esta negado le asigno a True
                if clause[0]>0: assignment[clause[0]]=1;
                # Si el literal esta negado le asigno a False
                else:assignment[abs(clause[0])]=0;
                # Pongo el update a True
                update= True
        

        #Etapa B: Literales que aparecen una unica vez

        # Cuento el numero de ocurrencias de cada variable y guardo el numero
        # de veces que aparece cada variable, alamacenandolo en una lista
        # en la misma posicion que el numero de la variable. Ej: Si x1 aparece 
        # 27 veces la lista tendra en lista[1] un 27.
        occurences= [0]*(num_literals+1)
        for clause in clauses:
            for literal in clause:
                occurences[abs(literal)]+=1
        
        # Despues de contar el numero de ocurrencias, accedo a la que tienen un
        # unico literal
        for o in range (len(occurences)):
            if occurences[o]==1:
                for clause in clauses:
                    flagborrarClausula=0
                    for literal in clause:
                        if abs(literal)==o: 
                            #Si el literal no esta negado le asigno a True
                            if literal>0: assignment[o]=1
                            # Si el literal esta negado le asigno a False
                            else: assignment[o]=0
                            # Pongo el update a True
                            update=True
                            # Pongo el flag a true para salir de la clausula ya que ya no 
                            # tengo que recorrer los demas literales
                            flagborrarClausula=1
                            break
                    if flagborrarClausula==1: break

        # Etapa C: Funcion de limpieza
        for clause in clauses:
            borrarClausulaFlag=0 
            # Hago una copia de la clausula para que no le afecten los removes
            copy_Clause= clause.copy()
            for literal in copy_Clause:
                # Si el literal esta negado
                if literal < 0:
                    # Si la asignacion esta a True el literal se evalua a False
                    # por lo que elimino el literal
                    if assignment[abs(literal)]==1: 
                        update= True
                        clause.remove(literal)
                    # Si la asignacion esta a False el literal se evalua a True
                    # por lo que elimino la clausula al completo y no evaluo los demas
                    # literales.
                    elif assignment[abs(literal)]==0: 
                        borrarClausulaFlag=1
                        break
                # Si el literal NO esta negado
                else:
                    # Si la asignacion esta a False el literal se evalua a False
                    # por lo que elimino el literal
                    if assignment[abs(literal)]==0: 
                        update= True
                        clause.remove(literal)
                    # Si la asignacion esta a True el literal se evalua a True
                    # por lo que elimino la clausula al completo y no evaluo los demas
                    # literales.
                    elif assignment[abs(literal)]==1: 
                        borrarClausulaFlag=1
                        break
            # Para eliminar una clausula la guardo en la lista clausulasParaEliminar
            if borrarClausulaFlag==1: 
                update= True
                clausulasParaEliminar.append(clause)
        # Elimino las clausulas guardadas en la lista 
        for delete in clausulasParaEliminar:
            if delete in clauses: clauses.remove(delete)


    if [] in clauses:
        return ([[1], [-1]], assignment)
    else:
        if (clauses == []) or (not update):
                return (clauses, assignment)  

    
