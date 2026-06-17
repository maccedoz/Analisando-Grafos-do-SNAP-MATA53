# Pacote de Algoritmos de Grafos (`algoritmos`)

Este diretório contém a implementação modularizada de 8 algoritmos clássicos de Teoria dos Grafos, implementados do zero (sem bibliotecas prontas de grafos para as operações internas).

---

## 📊 Grafo Base Utilizado — Zachary's Karate Club

Como base para ilustrar as execuções, utilizamos o grafo **Zachary's Karate Club** obtido via NetworkX. Os dados tratados estão em `data/karate_club_edges.csv` e `data/karate_adj_list.txt`.

*   **Vértices (N):** 34 (rotulados de 0 a 33)
*   **Arestas (M):** 78 (não-direcionadas, pesos sintéticos `w(u,v) = (u+v) mod 5 + 1` ∈ [1,5])
*   **Referência:** Zachary, W.W. (1977). *An Information Flow Model for Conflict and Fission in Small Groups.* Journal of Anthropological Research, 33(4), 452–473.

### Representação em Python (carregando do CSV)

```python
import csv

graph = {i: [] for i in range(34)}
weights = {}

with open('data/karate_club_edges.csv') as f:
    for row in csv.DictReader(f):
        u, v, w = int(row['source']), int(row['target']), float(row['weight'])
        graph[u].append(v)
        graph[v].append(u)
        weights[(u, v)] = w
        weights[(v, u)] = w
```

---

## 🛠️ Como Executar cada Algoritmo

Você pode importar e utilizar os algoritmos em seus próprios scripts Python a partir do pacote `algoritmos`. Certifique-se de que a pasta raiz do projeto esteja no seu `PYTHONPATH` ou configure o `sys.path`.

### 1. Busca em Largura (BFS)
Explora o grafo em largura a partir de um nó inicial.
```python
from algoritmos import bfs
ordem_visita = bfs(graph, start=0)
# Retorno esperado: todos os 34 nós em ordem BFS a partir do nó 0 (Mr. Hi)
```

### 2. Busca em Profundidade (DFS)
Explora o grafo em profundidade de forma recursiva.
```python
from algoritmos import dfs
ordem_visita = dfs(graph, start=0)
# Retorno esperado: todos os 34 nós em ordem DFS a partir do nó 0 (Mr. Hi)
```

### 3. Verificação de Eulerianidade
Determina se o grafo possui circuitos ou caminhos Eulerianos.
```python
from algoritmos import is_eulerian
status = is_eulerian(graph)
# Retorno esperado: "Não Euleriano" (múltiplos vértices com grau ímpar)
```

### 4. Algoritmo de Dijkstra
Caminho mínimo a partir de uma origem em grafos sem pesos negativos.
```python
from algoritmos import dijkstra
distancias = dijkstra(graph, start=0, weights=weights)
# Retorno: dicionário {nó: distância_mínima} a partir do nó 0
```

### 5. Algoritmo de Bellman-Ford
Caminho mínimo a partir de uma origem, permitindo pesos negativos e detectando ciclos negativos.
```python
from algoritmos import bellman_ford
distancias = bellman_ford(graph, start=0, weights=weights)
# Retorno: dicionário {nó: distância_mínima} a partir do nó 0
```

### 6. Algoritmo de Floyd-Warshall
Caminho mínimo entre todos os pares de vértices.
```python
from algoritmos import floyd_warshall
matriz_distancias = floyd_warshall(graph, weights=weights)
# Retorno: distâncias de todos os pares de nós
```

### 7. Algoritmo de Tarjan (SCC)
Identifica Componentes Fortemente Conexos (SCCs).
```python
from algoritmos import tarjan_scc
componentes = tarjan_scc(graph)
# Retorno esperado: [[todos os 34 nós]] (rede totalmente conexa)
```

### 8. Algoritmo de Kruskal (MST)
Gera a Árvore Geradora Mínima (MST).
```python
from algoritmos import kruskal_mst
arestas_mst, peso_total = kruskal_mst(graph, weights=weights)
# Retorno esperado: 33 arestas, peso_total = 51.0
```

---

## 🏃 Executando o Script Demonstrativo

Para rodar todos os algoritmos de uma vez usando o grafo do Karate Club e verificar os resultados completos, execute o seguinte script a partir da raiz do repositório:

```bash
python3 scripts/executar_algoritmos.py
```
