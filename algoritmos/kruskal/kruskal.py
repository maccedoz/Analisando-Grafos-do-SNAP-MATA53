def kruskal_mst(graph, weights, verbose=False):
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
        
    edges = []
    seen = set()
    for u in graph:
        for v in graph[u]:
            edge_key = (min(u, v), max(u, v))
            if edge_key not in seen:
                seen.add(edge_key)
                w = weights.get((u, v), 1.0)
                edges.append((w, u, v))
                
    edges.sort()
    
    if verbose:
        print("Kruskal: primeiro ordenamos todas as arestas pelo peso.")
        print(f"Total de arestas no grafo ordenadas: {len(edges)}")
    
    mst_edges = []
    total_weight = 0.0
    step = 1
    for w, u, v in edges:
        if union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if verbose:
                print(f"Passo {step}: Adicionamos a aresta ({u}, {v}) com peso {w:.1f} à MST.")
            step += 1
            if len(mst_edges) == len(graph) - 1:
                break
                
    if verbose:
        print(f"MST finalizada com {len(mst_edges)} arestas e peso total de {total_weight:.1f}")
        
    return mst_edges, total_weight

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

    print("Kruskal MST — Zachary's Karate Club")
    print("=" * 45)
    mst_edges, total_weight = kruskal_mst(graph, weights=weights)
    print(f"Arestas na MST ({len(mst_edges)} = N-1 = 34-1):")
    for u, v, w in mst_edges:
        print(f"  ({u:>2} — {v:>2})  peso: {w:.1f}")
    print(f"\nResultado: Peso total da MST = {total_weight:.1f}")
