def dfs(graph, start):
    """
    Busca em Profundidade (DFS).
    Retorna a ordem de visitação dos vértices a partir de um vértice inicial.
    """
    visited = set()
    order = []
    def dfs_visit(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs_visit(v)
    dfs_visit(start)
    return order
