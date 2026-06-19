import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algoritmos import bfs, dfs, is_eulerian, dijkstra, bellman_ford, floyd_warshall, tarjan_scc, kruskal_mst

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

def run_all_sequentially():
    print("======================================================================")
    print("EXECUTANDO ALGORITMOS NO GRAFO ZACHARY'S KARATE CLUB")
    print("======================================================================")
    print(f"Grafo de Entrada: {len(graph)} vértices, {sum(len(v) for v in graph.values())//2} arestas")
    print("----------------------------------------------------------------------")
    
    # BFS (Busca em Largura)
    print("\n[1] Busca em Largura (BFS) a partir do nó 0:")
    order_bfs = bfs(graph, start=0, verbose=False)
    print(f"    Ordem de visitação: {order_bfs}")
    
    # DFS (Busca em Profundidade)
    print("\n[2] Busca em Profundidade (DFS) a partir do nó 0:")
    order_dfs = dfs(graph, start=0, verbose=False)
    print(f"    Ordem de visitação: {order_dfs}")
    
    # Verificação de Eulerianidade
    print("\n[3] Verificação de Eulerianidade:")
    status_euler = is_eulerian(graph, verbose=False)
    print(f"    Status: {status_euler}")
    
    # Dijkstra
    print("\n[4] Algoritmo de Dijkstra a partir do nó 0 (Caminhos Mínimos):")
    dist_dijkstra = dijkstra(graph, start=0, weights=weights, verbose=False)
    for dest, d in sorted(dist_dijkstra.items()):
        print(f"    Distância de 0 a {dest:2d}: {d:.1f}")
    
    # Bellman-Ford
    print("\n[5] Algoritmo de Bellman-Ford a partir do nó 0:")
    dist_bf = bellman_ford(graph, start=0, weights=weights, verbose=False)
    if dist_bf is None:
        print("    Ciclo de custo negativo detectado!")
    else:
        for dest, d in sorted(dist_bf.items()):
            print(f"    Distância de 0 a {dest:2d}: {d:.1f}")
        
    # Floyd-Warshall
    print("\n[6] Algoritmo de Floyd-Warshall (ex: caminhos a partir do nó 0):")
    dist_fw = floyd_warshall(graph, weights=weights, verbose=False)
    for dest in sorted(dist_fw[0].keys()):
        print(f"    Distância de 0 a {dest:2d}: {dist_fw[0][dest]:.1f}")
    
    # Tarjan (Componentes Fortemente Conexos)
    print("\n[7] Algoritmo de Tarjan para Componentes Fortemente Conexos (SCC):")
    sccs = tarjan_scc(graph, verbose=False)
    print(f"    Componentes Encontrados: {len(sccs)}")
    
    # Kruskal (Árvore Geradora Mínima)
    print("\n[8] Algoritmo de Kruskal para Árvore Geradora Mínima (MST):")
    mst_edges, mst_weight = kruskal_mst(graph, weights=weights, verbose=False)
    print(f"    Arestas na MST: {len(mst_edges)}")
    print(f"    Peso total da MST: {mst_weight:.1f}")
    print("======================================================================\n")

def main():
    while True:
        print("\n========================================================")
        print("Escolha qual algoritmo você deseja rodar:")
        print("1 - BFS (Busca em Largura)")
        print("2 - DFS (Busca em Profundidade)")
        print("3 - Verificação de Eulerianidade")
        print("4 - Dijkstra (Caminhos Mínimos)")
        print("5 - Bellman-Ford (Caminhos Mínimos)")
        print("6 - Floyd-Warshall (Todos os Pares de Caminhos Mínimos)")
        print("7 - Tarjan (Componentes Fortemente Conexos)")
        print("8 - Kruskal (Árvore Geradora Mínima)")
        print("9 - Executar todos os algoritmos de forma simplificada")
        print("0 - Sair")
        print("========================================================")
        
        try:
            choice = input("Opção: ").strip()
            if choice == "0":
                print("Saindo do programa.")
                break
            elif choice == "1":
                bfs(graph, start=0, verbose=True)
            elif choice == "2":
                dfs(graph, start=0, verbose=True)
            elif choice == "3":
                is_eulerian(graph, verbose=True)
            elif choice == "4":
                dijkstra(graph, start=0, weights=weights, verbose=True)
            elif choice == "5":
                bellman_ford(graph, start=0, weights=weights, verbose=True)
            elif choice == "6":
                floyd_warshall(graph, weights=weights, verbose=True)
            elif choice == "7":
                tarjan_scc(graph, verbose=True)
            elif choice == "8":
                kruskal_mst(graph, weights=weights, verbose=True)
            elif choice == "9":
                run_all_sequentially()
            else:
                print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nSaindo do programa.")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
