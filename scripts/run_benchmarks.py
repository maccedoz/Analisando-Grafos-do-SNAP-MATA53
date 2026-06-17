import os
import sys
import time
import math
import numpy as np
import networkx as nx

# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos import bfs, dfs, is_eulerian, dijkstra, bellman_ford, floyd_warshall, tarjan_scc, kruskal_mst

# 1. Carregar o Grafo Zachary's Karate Club
G = nx.karate_club_graph()

# Converter para representação de lista de adjacência (dicionário de listas)
graph = {u: list(G.neighbors(u)) for u in G.nodes()}

# Gerar pesos determinísticos não-negativos para as arestas (para caminhos mínimos e MST)
weights = {}
for u, v in G.edges():
    w = (u + v) % 5 + 1
    weights[(u, v)] = w
    weights[(v, u)] = w

# Configurações do benchmark
N_TRIALS = 50  # n = 50 rodadas para o cálculo estatístico

# Número de execuções internas para cada algoritmo (para acumular tempo suficiente contra ruídos)
INNER_RUNS = {
    "BFS": 1000,
    "DFS": 1000,
    "Eulerian Check": 1000,
    "Dijkstra": 1000,
    "Bellman-Ford": 200,
    "Floyd-Warshall": 30,
    "Tarjan SCC": 1000,
    "Kruskal MST": 1000
}

results = {}

print("Iniciando benchmarks (n = 50 rodadas)...")

# Dicionário de funções para os algoritmos
funcs = {
    "BFS": lambda: bfs(graph, 0),
    "DFS": lambda: dfs(graph, 0),
    "Eulerian Check": lambda: is_eulerian(graph),
    "Dijkstra": lambda: dijkstra(graph, 0, weights),
    "Bellman-Ford": lambda: bellman_ford(graph, 0, weights),
    "Floyd-Warshall": lambda: floyd_warshall(graph, weights),
    "Tarjan SCC": lambda: tarjan_scc(graph),
    "Kruskal MST": lambda: kruskal_mst(graph, weights)
}

# Executar benchmarks
for name, func in funcs.items():
    inner_runs = INNER_RUNS[name]
    trial_times = []
    
    for _ in range(N_TRIALS):
        t0 = time.perf_counter()
        for _ in range(inner_runs):
            func()
        t1 = time.perf_counter()
        single_run_time = (t1 - t0) / inner_runs
        trial_times.append(single_run_time)
        
    trial_times = np.array(trial_times) * 1e6
    
    mean = np.mean(trial_times)
    std_dev = np.std(trial_times, ddof=1)
    
    z_critical = 1.96
    margin_of_error = z_critical * (std_dev / math.sqrt(N_TRIALS))
    ci_lower = mean - margin_of_error
    ci_upper = mean + margin_of_error
    
    results[name] = {
        "mean": mean,
        "std_dev": std_dev,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper
    }
    
    print(f"{name:15} | Média: {mean:8.2f} us | Desvio Padrão: {std_dev:8.2f} us | IC 95%: [{ci_lower:8.2f}, {ci_upper:8.2f}] us")

print("\n--- Resultados em Formato LaTeX (Linhas de Tabela) ---")
for name, stats in results.items():
    pt_name = {
        "BFS": "Busca em Largura (BFS)",
        "DFS": "Busca em Profundidade (DFS)",
        "Eulerian Check": "Verificação de Eulerianidade",
        "Dijkstra": "Algoritmo de Dijkstra",
        "Bellman-Ford": "Algoritmo de Bellman-Ford",
        "Floyd-Warshall": "Algoritmo de Floyd-Warshall",
        "Tarjan SCC": "Algoritmo de Tarjan (SCC)",
        "Kruskal MST": "Algoritmo de Kruskal (MST)"
    }[name]
    
    complexity = {
        "BFS": "$O(V + E)$",
        "DFS": "$O(V + E)$",
        "Eulerian Check": "$O(V + E)$",
        "Dijkstra": "$O((V + E) \\log V)$",
        "Bellman-Ford": "$O(V \\cdot E)$",
        "Floyd-Warshall": "$O(V^3)$",
        "Tarjan SCC": "$O(V + E)$",
        "Kruskal MST": "$O(E \\log V)$"
    }[name]
    
    mean_str = f"{stats['mean']:.3f}"
    std_str = f"{stats['std_dev']:.3f}"
    ci_str = f"[{stats['ci_lower']:.3f}, {stats['ci_upper']:.3f}]"
    
    row = f"    {pt_name} & {complexity} & {mean_str} & {std_str} & {ci_str} \\\\"
    print(row)
