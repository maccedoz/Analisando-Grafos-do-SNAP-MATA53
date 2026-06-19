def is_eulerian(graph, verbose=False):
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
        if verbose:
            print("Verificação de Eulerianidade:")
            print("  Grafo não possui vértices com arestas. É considerado Euleriano (Vazio).")
        return "Euleriano (Vazio)"
        
    if verbose:
        print("Verificação de Eulerianidade:")
        print(f"Passo 1: Verificar se o grafo é conexo a partir do nó {start_node}.")

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
            if verbose:
                print("  Grafo é desconexo!")
            return "Não Euleriano (Grafo Desconexo)"
            
    if verbose:
        print(f"  Grafo é conexo (todos os {len(graph)} nós são alcançáveis).")
        print("Passo 2: Contar nós de grau ímpar.")

    odd_nodes = [u for u in graph if len(graph[u]) % 2 != 0]
    odd_degrees = len(odd_nodes)
    
    if verbose:
        print(f"  Nós com grau ímpar ({odd_degrees} no total): {odd_nodes}")

    if odd_degrees == 0:
        if verbose:
            print("  Como não há nós com grau ímpar, o grafo é Euleriano.")
        return "Euleriano (Possui Circuito Euleriano)"
    elif odd_degrees == 2:
        if verbose:
            print("  Como há exatamente 2 nós com grau ímpar, o grafo é Semi-Euleriano.")
        return "Semi-Euleriano (Possui Caminho Euleriano)"
    else:
        if verbose:
            print("  Como há mais de 2 nós de grau ímpar, o grafo não é Euleriano.")
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
