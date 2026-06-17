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
