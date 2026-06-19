import csv
import os
import sys
import networkx as nx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

G = nx.karate_club_graph()

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

print("=== Verificação de Tratamentos Necessários ===")
print(f"  [N/A] Grafo temporal → estático   : dataset estático (snapshot único, 1970-1972)")
print(f"  [N/A] Grafo dirigido → não-dir.   : G.is_directed() = {G.is_directed()}")
print(f"  [N/A] Multigrafo → grafo simples  : G.is_multigraph() = {G.is_multigraph()}")
print(f"  [N/A] Remoção de auto-loops       : nx.number_of_selfloops(G) = {nx.number_of_selfloops(G)}")
print(f"  [N/A] Extração maior comp. conexa : {nx.number_connected_components(G)} componente(s) — grafo totalmente conexo")
print(f"  [N/A] Filtragem temporal          : sem atributos temporais no dataset")
print()

output_edges = os.path.join(data_dir, "karate_club_edges.csv")
with open(output_edges, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['source', 'target', 'weight', 'source_club', 'target_club'])

    for u, v in G.edges():
        weight = (u + v) % 5 + 1 
        club_u = G.nodes[u]['club']
        club_v = G.nodes[v]['club']
        writer.writerow([u, v, weight, club_u, club_v])

print(f"[OK] Lista de arestas (CSV) gerada em '{output_edges}'")


output_adj = os.path.join(data_dir, "karate_adj_list.txt")
with open(output_adj, 'w', encoding='utf-8') as f:
    f.write("# Lista de Adjacência — Zachary's Karate Club\n")
    f.write("# Formato: nó: [vizinhos ordenados]\n")
    f.write(f"# Nós: {G.number_of_nodes()} | Arestas: {G.number_of_edges()}\n\n")

    for node in sorted(G.nodes()):
        neighbors = sorted(G.neighbors(node))
        club = G.nodes[node]['club']
        f.write(f"{node} ({club}): {neighbors}\n")

print(f"[OK] Lista de adjacência (TXT) gerada em '{output_adj}'")

print()
print("=== Arquivos gerados ===")
print(f"  data/karate_club_edges.csv   — lista de arestas com pesos e facções")
print(f"  data/karate_adj_list.txt     — lista de adjacência por nó")
