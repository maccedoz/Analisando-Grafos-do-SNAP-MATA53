import os
import sys

# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos import bfs, dfs, is_eulerian, dijkstra, bellman_ford, floyd_warshall, tarjan_scc, kruskal_mst

# 1. Definir o grafo do artigo analisado (SIGMOD 2026 - CTLD)
# Nós: 1, 2, 3, 4, 5, 6, 7
# Arestas ponderadas: (1-2:2), (1-3:5), (2-4:1), (2-3:2), (3-5:3), (4-6:4), (4-5:2), (5-7:1)
graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

# Dicionário de pesos para caminhos mínimos e MST (grafo não direcionado, mapeando ambas as direções)
weights = {
    (1, 2): 2.0, (2, 1): 2.0,
    (1, 3): 5.0, (3, 1): 5.0,
    (2, 4): 1.0, (4, 2): 1.0,
    (2, 3): 2.0, (3, 2): 2.0,
    (3, 5): 3.0, (5, 3): 3.0,
    (4, 6): 4.0, (6, 4): 4.0,
    (4, 5): 2.0, (5, 4): 2.0,
    (5, 7): 1.0, (7, 5): 1.0
}

print("======================================================================")
print("🚀 EXECUTANDO ALGORITMOS NO GRAFO DO ARTIGO ANALISADO (SIGMOD 2026)")
print("======================================================================")
print(f"Grafo de Entrada: {len(graph)} vértices, 8 arestas")
for u, neighbors in graph.items():
    print(f"  Vértice {u} -> Conexões: {neighbors}")
print("----------------------------------------------------------------------")

# 1. BFS (Busca em Largura)
print("\n[1] Busca em Largura (BFS) a partir do nó 1:")
order_bfs = bfs(graph, start=1)
print(f"    Ordem de visitação: {order_bfs}")

# 2. DFS (Busca em Profundidade)
print("\n[2] Busca em Profundidade (DFS) a partir do nó 1:")
order_dfs = dfs(graph, start=1)
print(f"    Ordem de visitação: {order_dfs}")

# 3. Verificação de Eulerianidade
print("\n[3] Verificação de Eulerianidade:")
status_euler = is_eulerian(graph)
print(f"    Status: {status_euler}")

# 4. Dijkstra
print("\n[4] Algoritmo de Dijkstra a partir do nó 1 (Caminhos Mínimos):")
dist_dijkstra = dijkstra(graph, start=1, weights=weights)
for dest, d in sorted(dist_dijkstra.items()):
    print(f"    Distância de 1 a {dest}: {d}")

# 5. Bellman-Ford
print("\n[5] Algoritmo de Bellman-Ford a partir do nó 1:")
dist_bf = bellman_ford(graph, start=1, weights=weights)
if dist_bf is None:
    print("    Ciclo de custo negativo detectado!")
else:
    for dest, d in sorted(dist_bf.items()):
        print(f"    Distância de 1 a {dest}: {d}")

# 6. Floyd-Warshall
print("\n[6] Algoritmo de Floyd-Warshall (Todos contra Todos - ex: a partir do nó 1):")
dist_fw = floyd_warshall(graph, weights=weights)
for dest in sorted(dist_fw[1].keys()):
    print(f"    Distância de 1 a {dest}: {dist_fw[1][dest]}")

# 7. Tarjan SCC (Componentes Fortemente Conexos)
print("\n[7] Algoritmo de Tarjan para Componentes Fortemente Conexos (SCC):")
sccs = tarjan_scc(graph)
print(f"    Componentes Encontrados (total {len(sccs)}):")
for idx, scc in enumerate(sccs, 1):
    print(f"      Componente {idx}: {scc}")

# 8. Kruskal MST (Árvore Geradora Mínima)
print("\n[8] Algoritmo de Kruskal para Árvore Geradora Mínima (MST):")
mst_edges, mst_weight = kruskal_mst(graph, weights=weights)
print(f"    Arestas na MST (total {len(mst_edges)}):")
for u, v, w in mst_edges:
    print(f"      Aresta ({u} - {v}) com peso {w}")
print(f"    Peso total da MST: {mst_weight}")
print("======================================================================\n")
