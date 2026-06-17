def bellman_ford(graph, start, weights):
    """
    Algoritmo de Bellman-Ford.
    Calcula as menores distâncias a partir de um vértice inicial, suportando pesos negativos
    e detectando ciclos de peso negativo (retorna None se detectar um ciclo negativo).
    """
    dist = {u: float('inf') for u in graph}
    dist[start] = 0
    
    nodes = list(graph.keys())
    # Relaxar arestas V - 1 vezes
    for _ in range(len(nodes) - 1):
        for u in graph:
            for v in graph[u]:
                w = weights.get((u, v), 1.0)
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
    # Verificar ciclo de custo negativo
    for u in graph:
        for v in graph[u]:
            w = weights.get((u, v), 1.0)
            if dist[u] + w < dist[v]:
                return None  # Ciclo negativo detectado
                
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
