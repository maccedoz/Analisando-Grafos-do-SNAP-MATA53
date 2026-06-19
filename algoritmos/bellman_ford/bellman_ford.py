def bellman_ford(graph, start, weights, verbose=False):
    """
    Algoritmo de Bellman-Ford.
    Calcula as menores distâncias a partir de um vértice inicial, suportando pesos negativos
    e detectando ciclos de peso negativo (retorna None se detectar um ciclo negativo).
    """
    if verbose:
        print(f"Bellman-Ford: primeiro definimos distância 0 para a origem {start} e infinito para os outros.")
    dist = {u: float('inf') for u in graph}
    dist[start] = 0
    
    nodes = list(graph.keys())
    for i in range(1, len(nodes)):
        changed = False
        if verbose:
            print(f"Iteração {i}: relaxando todas as arestas...")
        updates = []
        for u in graph:
            for v in graph[u]:
                w = weights.get((u, v), 1.0)
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
                    updates.append(f"{v}(->{dist[v]:.1f})")
        if not changed:
            if verbose:
                print("  Nenhuma distância foi alterada nesta iteração. O algoritmo convergiu.")
            break
        else:
            if verbose:
                print(f"  Atualizações realizadas: {', '.join(updates[:8])}...")
                    
    neg_cycle = False
    for u in graph:
        for v in graph[u]:
            w = weights.get((u, v), 1.0)
            if dist[u] + w < dist[v]:
                neg_cycle = True
                break
                
    if neg_cycle:
        if verbose:
            print("Ciclo de custo negativo detectado!")
        return None  # Ciclo negativo detectado
        
    if verbose:
        print("Nenhum ciclo de custo negativo encontrado. Distâncias mínimas finais:")
        for dest in sorted(dist.keys()):
            print(f"  De {start} a {dest}: {dist[dest]:.1f}")
        
    return dist

if __name__ == "__main__":
    import csv, os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/karate_club_edges.csv')
    graph = {i: [] for i in range(34)}
    weights = {}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            u, v, w = int(row['source']), int(row['target']), float(row['weight'])
            graph[u].append(v); graph[v].append(u)
            weights[(u,v)] = w; weights[(v,u)] = w

    print("Bellman-Ford — Zachary's Karate Club (origem: nó 0 / Mr. Hi)")
    print("=" * 60)
    dist = bellman_ford(graph, start=0, weights=weights)
    if dist is None:
        print("Ciclo de peso negativo detectado!")
    else:
        print(f"{'Destino':>8}  {'Dist. Mínima':>12}")
        print("-" * 25)
        for dest in sorted(dist):
            print(f"  nó {dest:>2}  →  {dist[dest]:>6.1f}")
        print(f"\nResultado: sem ciclos negativos. Caminhos mínimos idênticos ao Dijkstra.")
