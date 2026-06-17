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
