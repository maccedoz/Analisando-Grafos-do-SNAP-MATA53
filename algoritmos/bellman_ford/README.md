# Algoritmo de Bellman-Ford

Calcula os caminhos mínimos a partir de um vértice de origem único. Diferente do Dijkstra, suporta arestas com pesos negativos e é capaz de detectar ciclos negativos de custo (retornando `None` nesses casos). Opera relaxando todas as arestas do grafo $|V| - 1$ vezes, resultando em uma complexidade de $O(V \cdot E)$.

---

## 📈 Execução no Grafo Zachary's Karate Club

Rodando o Bellman-Ford a partir do nó inicial `1`:

*   **Entrada:** Grafo de 7 vértices, pesos e nó inicial `1`.
*   **Resultados de Distância Mínima:**
    *   `1 -> 1`: $0.0$
    *   `1 -> 2`: $2.0$
    *   `1 -> 3`: $4.0$
    *   `1 -> 4`: $3.0$
    *   `1 -> 5`: $5.0$
    *   `1 -> 6`: $7.0$
    *   `1 -> 7`: $6.0$

## 💻 Exemplo de Uso em Python

```python
from algoritmos import bellman_ford

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

distancias = bellman_ford(graph, start=1, weights=weights)
print(distancias)
# {1: 0, 2: 2.0, 3: 4.0, 4: 3.0, 5: 5.0, 6: 7.0, 7: 6.0}
```
