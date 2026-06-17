import csv
import os
import sys

# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos import bfs, dfs, is_eulerian, dijkstra, bellman_ford, floyd_warshall, tarjan_scc, kruskal_mst

# ──────────────────────────────────────────────
# Carregar o grafo do Zachary's Karate Club a partir do CSV tratado
# ──────────────────────────────────────────────
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
csv_path = os.path.join(base_dir, 'data', 'karate_club_edges.csv')

graph = {i: [] for i in range(34)}
weights = {}

with open(csv_path, encoding='utf-8') as f:
    for row in csv.DictReader(f):
        u, v, w = int(row['source']), int(row['target']), float(row['weight'])
        graph[u].append(v)
        graph[v].append(u)
        weights[(u, v)] = w
        weights[(v, u)] = w

print("======================================================================")
print("🚀 EXECUTANDO ALGORITMOS NO GRAFO ZACHARY'S KARATE CLUB")
print("======================================================================")
print(f"Grafo de Entrada: {len(graph)} vértices, {sum(len(v) for v in graph.values())//2} arestas")
print("----------------------------------------------------------------------")

# 1. BFS (Busca em Largura)
print("\n[1] Busca em Largura (BFS) a partir do nó 0 (Mr. Hi):")
order_bfs = bfs(graph, start=0)
print(f"    Ordem de visitação: {order_bfs}")

# 2. DFS (Busca em Profundidade)
print("\n[2] Busca em Profundidade (DFS) a partir do nó 0 (Mr. Hi):")
order_dfs = dfs(graph, start=0)
print(f"    Ordem de visitação: {order_dfs}")

# 3. Verificação de Eulerianidade
print("\n[3] Verificação de Eulerianidade:")
status_euler = is_eulerian(graph)
print(f"    Status: {status_euler}")

# 4. Dijkstra
print("\n[4] Algoritmo de Dijkstra a partir do nó 0 (Caminhos Mínimos):")
dist_dijkstra = dijkstra(graph, start=0, weights=weights)
for dest, d in sorted(dist_dijkstra.items())[:10]:
    print(f"    Distância de 0 a {dest:2d}: {d}")
print(f"    ... (mostrando 10 de {len(dist_dijkstra)} nós)")

# 5. Bellman-Ford
print("\n[5] Algoritmo de Bellman-Ford a partir do nó 0:")
dist_bf = bellman_ford(graph, start=0, weights=weights)
if dist_bf is None:
    print("    Ciclo de custo negativo detectado!")
else:
    for dest, d in sorted(dist_bf.items())[:10]:
        print(f"    Distância de 0 a {dest:2d}: {d}")
    print(f"    ... (mostrando 10 de {len(dist_bf)} nós)")

# 6. Floyd-Warshall
print("\n[6] Algoritmo de Floyd-Warshall (ex: caminhos a partir do nó 0):")
dist_fw = floyd_warshall(graph, weights=weights)
for dest in sorted(dist_fw[0].keys())[:10]:
    print(f"    Distância de 0 a {dest:2d}: {dist_fw[0][dest]}")
print(f"    ... (mostrando 10 de {len(dist_fw[0])} nós)")

# 7. Tarjan SCC (Componentes Fortemente Conexos)
print("\n[7] Algoritmo de Tarjan para Componentes Fortemente Conexos (SCC):")
sccs = tarjan_scc(graph)
print(f"    Componentes Encontrados: {len(sccs)} (esperado: 1, grafo totalmente conexo)")

# 8. Kruskal MST (Árvore Geradora Mínima)
print("\n[8] Algoritmo de Kruskal para Árvore Geradora Mínima (MST):")
mst_edges, mst_weight = kruskal_mst(graph, weights=weights)
print(f"    Arestas na MST: {len(mst_edges)} (esperado: {len(graph)-1} = N-1)")
print(f"    Peso total da MST: {mst_weight} (esperado: 51.0)")

print("======================================================================\n")
