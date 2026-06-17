def is_eulerian(graph):
    """
    Verificação de Eulerianidade do grafo.
    Determina se um grafo não-direcionado é Euleriano, Semi-Euleriano ou Não Euleriano.
    """
    start_node = None
    for u in graph:
        if len(graph[u]) > 0:
            start_node = u
            break
            
    if start_node is None:
        return "Euleriano (Vazio)"
        
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    while queue:
        curr = queue.pop(0)
        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
                
    for u in graph:
        if len(graph[u]) > 0 and u not in visited:
            return "Não Euleriano (Grafo Desconexo)"
            
    odd_degrees = sum(1 for u in graph if len(graph[u]) % 2 != 0)
    
    if odd_degrees == 0:
        return "Euleriano (Possui Circuito Euleriano)"
    elif odd_degrees == 2:
        return "Semi-Euleriano (Possui Caminho Euleriano)"
    else:
        return "Não Euleriano"

if __name__ == "__main__":
    import csv, os, sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/karate_club_edges.csv')
    graph = {i: [] for i in range(34)}
    with open(csv_path) as f:
        for row in csv.DictReader(f):
            u, v = int(row['source']), int(row['target'])
            graph[u].append(v); graph[v].append(u)

    odd = [u for u in graph if len(graph[u]) % 2 != 0]
    print("Eulerianidade — Zachary's Karate Club")
    print("=" * 45)
    print(f"Nós com grau ímpar: {len(odd)} → {odd}")
    result = is_eulerian(graph)
    print(f"Resultado: {result}")
    print(f"\nExplicação: como {len(odd)} > 2 nós têm grau ímpar, não existe circuito nem caminho euleriano.")
