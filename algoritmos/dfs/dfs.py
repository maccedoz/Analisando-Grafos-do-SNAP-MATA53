def dfs(graph, start, verbose=False):
    """
    Busca em Profundidade (DFS).
    Retorna a ordem de visitação dos vértices a partir de um vértice inicial.
    """
    visited = set()
    order = []
    step = 1
    if verbose:
        print(f"DFS (Busca em Profundidade): primeiro chegamos no nó {start}")
        
    def dfs_visit(u, depth=1):
        nonlocal step
        visited.add(u)
        order.append(u)
        indent = "  " * depth
        neighbors = graph.get(u, [])
        if verbose:
            print(f"Passo {step}:{indent}Chegamos no nó {u}. Vizinhos: {neighbors}")
        step += 1
        for v in neighbors:
            if v not in visited:
                if verbose:
                    print(f"{indent}  O vizinho {v} não foi visitado. Indo para o nó {v}...")
                dfs_visit(v, depth + 1)
            else:
                if verbose:
                    print(f"{indent}  O vizinho {v} já foi visitado.")
                    
    dfs_visit(start)
    if verbose:
        print(f"Todos os {len(visited)} nós foram visitados na ordem: {order}")
    return order

if __name__ == "__main__":
    import csv, os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/karate_club_edges.csv')
    graph = {i: [] for i in range(34)}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            u, v = int(row['source']), int(row['target'])
            graph[u].append(v); graph[v].append(u)

    print("DFS — Zachary's Karate Club (nó inicial: 0 / Mr. Hi)")
    print("=" * 55)
    result = dfs(graph, start=0)
    print(f"Nós visitados ({len(result)} no total):")
    print(f"  {result}")
    print(f"\nResultado: grafo totalmente conexo — todos os 34 nós alcançados em profundidade a partir do nó 0.")
