def floyd_warshall(graph, weights):
    """
    Algoritmo de Floyd-Warshall.
    Calcula as menores distâncias entre todos os pares de vértices do grafo.
    """
    nodes = list(graph.keys())
    # Inicializar matriz de distâncias
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0
        for v in graph.get(u, []):
            dist[u][v] = weights.get((u, v), 1.0)
            
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
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

    print("Floyd-Warshall — Zachary's Karate Club (todos os pares)")
    print("=" * 55)
    dist = floyd_warshall(graph, weights=weights)
    print("Amostra: caminhos mínimos a partir do nó 0:")
    print(f"  {'Destino':>8}  {'Dist. Mínima':>12}")
    print("  " + "-" * 25)
    for dest in sorted(dist[0])[:10]:
        print(f"    nó {dest:>2}  →  {dist[0][dest]:>6.1f}")
    print(f"  ... (34×34 = 1156 pares calculados)")
    max_d = max(dist[u][v] for u in dist for v in dist[u] if dist[u][v] != float('inf'))
    print(f"\nResultado: diâmetro ponderado do grafo = {max_d:.1f}")
