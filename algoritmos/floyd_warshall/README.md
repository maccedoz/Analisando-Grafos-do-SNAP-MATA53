# Algoritmo de Floyd-Warshall

Resolve o problema de caminhos mínimos entre todos os pares de vértices de forma simultânea (todos contra todos), utilizando programação dinâmica. Possui complexidade teórica de $O(V^3)$.

---

## 📈 Execução no Grafo do Artigo (SIGMOD 2026)

*   **Entrada:** Grafo de 7 vértices e pesos associados.
*   **Saída Parcial (Distâncias a partir do vértice 1):**
    *   `1 -> 1`: $0.0$
    *   `1 -> 2`: $2.0$
    *   `1 -> 3`: $4.0$
    *   `1 -> 4`: $3.0$
    *   `1 -> 5`: $5.0$
    *   `1 -> 6`: $7.0$
    *   `1 -> 7`: $6.0$

## 💻 Exemplo de Uso em Python

```python
from algoritmos import floyd_warshall

graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

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

matriz_dist = floyd_warshall(graph, weights=weights)
# Para obter a menor distância entre 1 e 7:
print(matriz_dist[1][7]) # 6.0
```
