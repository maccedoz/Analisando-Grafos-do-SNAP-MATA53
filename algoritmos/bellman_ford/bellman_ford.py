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
