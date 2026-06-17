# Pacote de Algoritmos de Grafos (`algoritmos`)

Este diretório contém a implementação modularizada de 8 algoritmos clássicos de Teoria dos Grafos, implementados do zero (sem bibliotecas prontas de grafos para as operações internas).

---

## 📊 Grafo Base Utilizado (Artigo SIGMOD 2026 - CTLD)

Como base para ilustrar as execuções, utilizamos o grafo ponderado e não direcionado do artigo de referência de busca kNN em redes viárias:

*   **Vértices ($V$):** `1, 2, 3, 4, 5, 6, 7`
*   **Arestas com pesos ($E$):**
    *   `(1 - 2)` com peso $2.0$
    *   `(1 - 3)` com peso $5.0$
    *   `(2 - 4)` com peso $1.0$
    *   `(2 - 3)` com peso $2.0$
    *   `(3 - 5)` com peso $3.0$
    *   `(4 - 6)` com peso $4.0$
    *   `(4 - 5)` com peso $2.0$
    *   `(5 - 7)` com peso $1.0$

### Representação em Python (Lista de Adjacência e Pesos)

```python
# Lista de Adjacência (representando o grafo não-direcionado)
graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

# Dicionário de pesos (mapeado para ambos os sentidos)
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
```

---

## 🛠️ Como Executar cada Algoritmo

Você pode importar e utilizar os algoritmos em seus próprios scripts Python a partir do pacote `algoritmos`. Certifique-se de que a pasta raiz do projeto esteja no seu `PYTHONPATH` ou configure o `sys.path`.

### 1. Busca em Largura (BFS)
Explora o grafo em largura a partir de um nó inicial.
```python
from algoritmos import bfs
ordem_visita = bfs(graph, start=1)
# Retorno esperado: [1, 2, 3, 4, 5, 6, 7]
```

### 2. Busca em Profundidade (DFS)
Explora o grafo em profundidade de forma recursiva.
```python
from algoritmos import dfs
ordem_visita = dfs(graph, start=1)
# Retorno esperado: [1, 2, 4, 6, 5, 3, 7]
```

### 3. Verificação de Eulerianidade
Determina se o grafo possui circuitos ou caminhos Eulerianos.
```python
from algoritmos import is_eulerian
status = is_eulerian(graph)
# Retorno esperado: "Não Euleriano" (pois possui mais de 2 vértices de grau ímpar)
```

### 4. Algoritmo de Dijkstra
Caminho mínimo a partir de uma origem em grafos sem pesos negativos.
```python
from algoritmos import dijkstra
distancias = dijkstra(graph, start=1, weights=weights)
# Retorno esperado: {1: 0, 2: 2.0, 3: 4.0, 4: 3.0, 5: 5.0, 6: 7.0, 7: 6.0}
```

### 5. Algoritmo de Bellman-Ford
Caminho mínimo a partir de uma origem, permitindo arestas negativas e detectando ciclos negativos.
```python
from algoritmos import bellman_ford
distancias = bellman_ford(graph, start=1, weights=weights)
# Retorno esperado: {1: 0, 2: 2.0, 3: 4.0, 4: 3.0, 5: 5.0, 6: 7.0, 7: 6.0}
```

### 6. Algoritmo de Floyd-Warshall
Caminho mínimo entre todos os pares de vértices.
```python
from algoritmos import floyd_warshall
matriz_distancias = floyd_warshall(graph, weights=weights)
# Retorno de distâncias a partir do nó 1: matriz_distancias[1] -> {1: 0, 2: 2.0, ...}
```

### 7. Algoritmo de Tarjan (SCC)
Identifica Componentes Fortemente Conexos (SCCs).
```python
from algoritmos import tarjan_scc
componentes = tarjan_scc(graph)
# Retorno esperado: [[7, 3, 5, 6, 4, 2, 1]] (um único SCC unificado)
```

### 8. Algoritmo de Kruskal (MST)
Gera a Árvore Geradora Mínima (MST).
```python
from algoritmos import kruskal_mst
arestas_mst, peso_total = kruskal_mst(graph, weights=weights)
# Retorno esperado: (arestas_mst, peso_total = 12.0)
```

---

## 🏃 Executando o Script Demonstrativo

Para rodar todos os algoritmos de uma vez usando o grafo do artigo e verificar os resultados completos, execute o seguinte script a partir da raiz do repositório:

```bash
python3 scripts/executar_algoritmos.py
```
