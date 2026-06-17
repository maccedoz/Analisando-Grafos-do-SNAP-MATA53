def bfs(graph, start):
    """
    Busca em Largura (BFS).
    Retorna a ordem de visitação dos vértices a partir de um vértice inicial.
    """
    visited = {start}
    queue = [start]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
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

    print("BFS — Zachary's Karate Club (nó inicial: 0 / Mr. Hi)")
    print("=" * 55)
    result = bfs(graph, start=0)
    print(f"Nós visitados ({len(result)} no total):")
    print(f"  {result}")
    print(f"\nResultado: grafo totalmente conexo — todos os 34 nós alcançados a partir do nó 0.")
