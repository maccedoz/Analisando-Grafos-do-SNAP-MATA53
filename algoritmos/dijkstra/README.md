# Algoritmo de Dijkstra

Algoritmo clássico de busca de caminhos mínimos de única origem para grafos com pesos não negativos. Utiliza uma fila de prioridades baseada em heap binária para garantir complexidade de $O((V + E) \log V)$.

---

## 📈 Execução no Grafo Zachary's Karate Club

Rodando o Dijkstra a partir do nó inicial `1`:

*   **Entrada:** Grafo de 7 vértices, pesos e nó inicial `1`.
*   **Resultados de Distância Mínima:**
    *   `1 -> 1`: $0.0$
    *   `1 -> 2`: $2.0$ (via direta 1-2)
    *   `1 -> 3`: $4.0$ (via 1-2-3)
    *   `1 -> 4`: $3.0$ (via 1-2-4)
    *   `1 -> 5`: $5.0$ (via 1-2-4-5)
    *   `1 -> 6`: $7.0$ (via 1-2-4-6)
    *   `1 -> 7`: $6.0$ (via 1-2-4-5-7)

## 💻 Exemplo de Uso em Python

```python
from algoritmos import dijkstra

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

distancias = dijkstra(graph, start=1, weights=weights)
print(distancias)
# {1: 0, 2: 2.0, 3: 4.0, 4: 3.0, 5: 5.0, 6: 7.0, 7: 6.0}
```
