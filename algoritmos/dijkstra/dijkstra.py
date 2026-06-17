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

    print("Dijkstra — Zachary's Karate Club (origem: nó 0 / Mr. Hi)")
    print("=" * 55)
    dist = dijkstra(graph, start=0, weights=weights)
    print(f"{'Destino':>8}  {'Dist. Mínima':>12}")
    print("-" * 25)
    for dest in sorted(dist):
        print(f"  nó {dest:>2}  →  {dist[dest]:>6.1f}")
    print(f"\nResultado: menor distância total = {min(dist[v] for v in dist if v != 0):.1f} (nó mais próximo: {min(dist, key=lambda v: dist[v] if v != 0 else float('inf'))})")
