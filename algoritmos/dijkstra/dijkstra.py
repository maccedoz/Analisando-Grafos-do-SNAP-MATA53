import heapq

def dijkstra(graph, start, weights):
    """
    Algoritmo de Dijkstra.
    Calcula as menores distâncias a partir de um vértice inicial em um grafo com pesos não-negativos.
    """
    dist = {u: float('inf') for u in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in graph.get(u, []):
            w = weights.get((u, v), 1.0)
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
