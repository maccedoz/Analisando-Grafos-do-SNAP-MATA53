def kruskal_mst(graph, weights):
    """
    Algoritmo de Kruskal.
    Calcula a Árvore Geradora Mínima (MST) de um grafo não direcionado ponderado.
    Retorna uma tupla (lista_de_arestas_da_mst, peso_total).
    """
    parent = {u: u for u in graph}
    rank = {u: 0 for u in graph}
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
        
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1
            return True
        return False
        
    # Coletar todas as arestas únicas (garantindo u < v para evitar duplicadas no grafo não direcionado)
    edges = []
    seen = set()
    for u in graph:
        for v in graph[u]:
            edge_key = (min(u, v), max(u, v))
            if edge_key not in seen:
                seen.add(edge_key)
                w = weights.get((u, v), 1.0)
                edges.append((w, u, v))
                
    # Ordenar arestas por peso
    edges.sort()
    
    mst_edges = []
    total_weight = 0.0
    for w, u, v in edges:
        if union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == len(graph) - 1:
                break
                
    return mst_edges, total_weight
