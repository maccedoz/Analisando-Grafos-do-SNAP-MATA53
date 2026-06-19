def tarjan_scc(graph, verbose=False):
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
    step = 1
    
    if verbose:
        print("Tarjan: primeiro inicializamos a busca em profundidade para encontrar componentes fortemente conexos.")

    def strongconnect(u):
        nonlocal index_counter, step
        indices[u] = index_counter
        lowlink[u] = index_counter
        index_counter += 1
        stack.append(u)
        on_stack.add(u)
        
        if verbose:
            print(f"Passo {step}: DFS visita o nó {u}. index={indices[u]}, lowlink={lowlink[u]}")
        step += 1
        
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
            if verbose:
                print(f"  Encontrado componente fortemente conexo: {sorted(scc)}")
            
    for u in graph:
        if u not in indices:
            strongconnect(u)
            
    if verbose:
        print(f"Total de componentes encontrados: {len(sccs)}")
            
    return sccs

if __name__ == "__main__":
    import csv, os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/karate_club_edges.csv')
    graph = {i: [] for i in range(34)}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            u, v = int(row['source']), int(row['target'])
            graph[u].append(v); graph[v].append(u)

    print("Tarjan SCC — Zachary's Karate Club")
    print("=" * 45)
    sccs = tarjan_scc(graph)
    print(f"Componentes Fortemente Conexos encontrados: {len(sccs)}")
    for i, scc in enumerate(sccs, 1):
        print(f"  SCC {i}: {sorted(scc)} (tamanho: {len(scc)})")
    print(f"\nResultado: {len(sccs)} componente(s) — a rede é totalmente conexa.")
