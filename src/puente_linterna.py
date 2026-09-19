import itertools
import SimpleSearch as sp

def crear_sucesor(todas_las_personas):
    """
    Retorna la función sucesor adaptada a un conjunto particular de personas.
    """
    def sucesor(nodo):
        personas_izq, pos_linterna = nodo.state
        sucesores = []
        
        if pos_linterna == 0:
            for r in (1, 2):
                for grupo in itertools.combinations(personas_izq, r):
                    grupo_set = set(grupo)
                    nueva_izq = frozenset(personas_izq - grupo_set)
                    nuevo_estado = (nueva_izq, 1)
                    costo_paso = max(grupo)
                    op_nombre = f"Cruzar a derecha: {list(grupo)}"
                    
                    hijo = sp.Node(
                        state=nuevo_estado,
                        parent=nodo,
                        depth=nodo.depth + 1,
                        step_cost=costo_paso,
                        op=op_nombre
                    )
                    sucesores.append(hijo)
        else:
            personas_der = set(todas_las_personas) - set(personas_izq)
            for r in (1, 2):
                for grupo in itertools.combinations(personas_der, r):
                    nueva_izq = frozenset(personas_izq | set(grupo))
                    nuevo_estado = (nueva_izq, 0)
                    costo_paso = max(grupo)
                    op_nombre = f"Regresar a izquierda: {list(grupo)}"
                    
                    hijo = sp.Node(
                        state=nuevo_estado,
                        parent=nodo,
                        depth=nodo.depth + 1,
                        step_cost=costo_paso,
                        op=op_nombre
                    )
                    sucesores.append(hijo)
                    
        return sucesores

    return sucesor

def meta(nodo, goal_state=None):
    personas_izq, pos_linterna = nodo.state
    return len(personas_izq) == 0 and pos_linterna == 1

def h1_maximo(nodo, goal_state=None):
    personas_izq, _ = nodo.state
    return max(personas_izq) if personas_izq else 0

def h2_promedio(nodo, goal_state=None):
    personas_izq, _ = nodo.state
    return (sum(personas_izq) / len(personas_izq)) if personas_izq else 0

def h0_nula(nodo, goal_state=None):
    return 0