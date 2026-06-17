import os
import sys
import random
import numpy as np
import networkx as nx

# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ──────────────────────────────────────────────
# REPRESENTAÇÃO DO GRAFO E AUXILIARES
# ──────────────────────────────────────────────
G = nx.karate_club_graph()
N = len(G.nodes())
M = len(G.edges())

# Adjacency list from scratch
def get_adj_list(graph_nx):
    return {u: list(graph_nx.neighbors(u)) for u in graph_nx.nodes()}

adj_list = get_adj_list(G)

# ──────────────────────────────────────────────
# ALGORITMOS DE GRAFO DESDE O INÍCIO (FROM SCRATCH)
# ──────────────────────────────────────────────

# 1. BFS para distância mínima de um nó para todos os outros
def bfs_distances(graph, start):
    dist = {u: float('inf') for u in graph}
    dist[start] = 0
    queue = [start]
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

# 2. Comprimento Médio dos Caminhos (L)
def average_path_length(graph):
    total_dist = 0
    pairs = 0
    nodes = list(graph.keys())
    for u in nodes:
        dists = bfs_distances(graph, u)
        for v in nodes:
            if u != v and dists[v] != float('inf'):
                total_dist += dists[v]
                pairs += 1
    if pairs == 0:
        return float('inf')
    return total_dist / pairs

# 3. Coeficiente de Clusterização Local e Médio (C)
def clustering_coefficient(graph):
    c_vals = {}
    for u in graph:
        neighbors = graph[u]
        k = len(neighbors)
        if k < 2:
            c_vals[u] = 0.0
            continue
        edges_between_neighbors = 0
        neighbors_set = set(neighbors)
        for v in neighbors:
            for w in graph[v]:
                if w in neighbors_set:
                    edges_between_neighbors += 1
        edges_between_neighbors = edges_between_neighbors // 2
        possible_edges = k * (k - 1) // 2
        c_vals[u] = edges_between_neighbors / possible_edges
    return np.mean(list(c_vals.values()))

# 4. Encontrar componentes conexos
def get_connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            comp = []
            queue = [node]
            visited.add(node)
            while queue:
                u = queue.pop(0)
                comp.append(u)
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            components.append(comp)
    return components

# ──────────────────────────────────────────────
# APÊNDICE A: PROPRIEDADE SMALL-WORLD
# ──────────────────────────────────────────────

# Gerar grafo aleatório G(N, M) conexo
def generate_random_connected_graph(num_nodes, num_edges):
    while True:
        rand_graph = {i: [] for i in range(num_nodes)}
        possible_pairs = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]
        selected_edges = random.sample(possible_pairs, num_edges)
        for u, v in selected_edges:
            rand_graph[u].append(v)
            rand_graph[v].append(u)
        if len(get_connected_components(rand_graph)) == 1:
            return rand_graph

print("Calculando propriedade Small-world...")
C_obs = clustering_coefficient(adj_list)
L_obs = average_path_length(adj_list)

C_rands = []
L_rands = []
for _ in range(100):
    rg = generate_random_connected_graph(N, M)
    C_rands.append(clustering_coefficient(rg))
    L_rands.append(average_path_length(rg))

C_rand = np.mean(C_rands)
L_rand = np.mean(L_rands)

sigma_sw = (C_obs / C_rand) / (L_obs / L_rand)

print(f"C_obs: {C_obs:.4f} | C_rand: {C_rand:.4f} | Razão C: {C_obs/C_rand:.4f}")
print(f"L_obs: {L_obs:.4f} | L_rand: {L_rand:.4f} | Razão L: {L_obs/L_rand:.4f}")
print(f"Small-worldness sigma: {sigma_sw:.4f}")

# ──────────────────────────────────────────────
# APÊNDICE B: LEI DE POTÊNCIA
# ──────────────────────────────────────────────
print("\nAnálise de Lei de Potência...")
degrees = [len(adj_list[u]) for u in adj_list]
unique_degrees, counts = np.unique(degrees, return_counts=True)
log_k = np.log(unique_degrees)
log_freq = np.log(counts)
slope, intercept = np.polyfit(log_k, log_freq, 1)
gamma = -slope
print(f"Expoente gamma estimado via log-log linear: {gamma:.4f}")

# ──────────────────────────────────────────────
# APÊNDICE C: ROBUSTEZ DA REDE
# ──────────────────────────────────────────────
print("\nSimulações de Robustez da Rede...")

num_to_remove = int(round(N * 0.05))
random_trials = 1000
lcc_sizes_rand = []
l_vals_rand = []

for _ in range(random_trials):
    nodes_to_remove = random.sample(list(adj_list.keys()), num_to_remove)
    subgraph = {u: [v for v in adj_list[u] if v not in nodes_to_remove] 
                for u in adj_list if u not in nodes_to_remove}
    
    components = get_connected_components(subgraph)
    lcc_size = max(len(c) for c in components)
    lcc_sizes_rand.append(lcc_size)
    
    lcc_nodes = max(components, key=len)
    lcc_graph = {u: [v for v in subgraph[u] if v in lcc_nodes] for u in lcc_nodes}
    l_lcc = average_path_length(lcc_graph)
    l_vals_rand.append(l_lcc)

avg_lcc_size_rand = np.mean(lcc_sizes_rand)
avg_l_rand = np.mean(l_vals_rand)

print(f"Remoção Aleatória (5% = {num_to_remove} nós):")
print(f"  Tamanho médio do LCC: {avg_lcc_size_rand:.2f} nós (original: {N})")
print(f"  Caminho médio no LCC: {avg_l_rand:.4f} saltos (original: {L_obs:.4f})")

# B. Remoção dos 5% mais centrais
degrees_sorted = sorted([(len(adj_list[u]), u) for u in adj_list], reverse=True)
nodes_central = [u for deg, u in degrees_sorted[:num_to_remove]]
print(f"Nós mais centrais removidos: {nodes_central} (graus: {[len(adj_list[u]) for u in nodes_central]})")

subgraph_targeted = {u: [v for v in adj_list[u] if v not in nodes_central] 
                     for u in adj_list if u not in nodes_central}

components_targeted = get_connected_components(subgraph_targeted)
lcc_size_targeted = max(len(c) for c in components_targeted)
lcc_nodes_targeted = max(components_targeted, key=len)
lcc_graph_targeted = {u: [v for v in subgraph_targeted[u] if v in lcc_nodes_targeted] for u in lcc_nodes_targeted}
l_targeted = average_path_length(lcc_graph_targeted)

print(f"Remoção Direcionada (5% mais centrais):")
print(f"  Tamanho do LCC: {lcc_size_targeted} nós (original: {N})")
print(f"  Caminho médio no LCC: {l_targeted:.4f} saltos (original: {L_obs:.4f})")
print(f"  Componentes conexos resultantes: {len(components_targeted)} (tamanhos: {[len(c) for c in components_targeted]})")
