# Algoritmo de Kruskal (MST)

O algoritmo de Kruskal constrói a Árvore Geradora Mínima (MST) de um grafo não direcionado conectado. Ordena todas as arestas por peso e utiliza uma estrutura de dados de conjuntos disjuntos (Union-Find) com compressão de caminhos para evitar ciclos. A complexidade é de $O(E \log V)$.

---

## 📈 Execução no Grafo Zachary's Karate Club

*   **Entrada:** Grafo de 7 vértices e pesos associados.
*   **Arestas Selecionadas para a MST:**
    *   `(2 - 4)` com peso $1.0$
    *   `(5 - 7)` com peso $1.0$
    *   `(1 - 2)` com peso $2.0$
    *   `(2 - 3)` com peso $2.0$
    *   `(4 - 5)` com peso $2.0$
    *   `(4 - 6)` com peso $4.0$
*   **Peso Total da MST:** $12.0$

## 💻 Exemplo de Uso em Python

```python
from algoritmos import kruskal_mst

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

arestas_mst, peso_total = kruskal_mst(graph, weights=weights)
print(peso_total) # 12.0
```
