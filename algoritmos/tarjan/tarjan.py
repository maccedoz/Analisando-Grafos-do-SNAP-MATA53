def tarjan_scc(graph):
    """
    Algoritmo de Tarjan.
    Encontra as componentes fortemente conexas (SCCs) de um grafo direcionado.
    """
    index_counter = 0
    indices = {}
    lowlink = {}
    on_stack = set()
    stack = []
    sccs = []
    
    def strongconnect(u):
        nonlocal index_counter
        indices[u] = index_counter
        lowlink[u] = index_counter
        index_counter += 1
        stack.append(u)
        on_stack.add(u)
        
        for v in graph.get(u, []):
            if v not in indices:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif v in on_stack:
                lowlink[u] = min(lowlink[u], indices[v])
                
        if lowlink[u] == indices[u]:
            scc = []
            while True:
                v = stack.pop()
                on_stack.remove(v)
                scc.append(v)
                if v == u:
                    break
            sccs.append(scc)
            
    for u in graph:
        if u not in indices:
            strongconnect(u)
            
    return sccs
