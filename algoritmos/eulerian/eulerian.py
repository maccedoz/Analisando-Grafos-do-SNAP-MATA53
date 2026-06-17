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
