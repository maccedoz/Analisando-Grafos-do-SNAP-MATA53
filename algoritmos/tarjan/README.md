# Algoritmo de Tarjan para Componentes Fortemente Conexos (SCC)

O algoritmo de Tarjan identifica os Componentes Fortemente Conexos (SCCs) de um grafo direcionado usando uma única busca em profundidade (DFS) auxiliada por uma pilha e vetores de controle de índice/lowlink. A complexidade é linear, de $O(V + E)$.

---

## 📈 Execução no Grafo Zachary's Karate Club

Embora o grafo do artigo seja bidirecional (tratado como não direcionado), as arestas são inseridas nas duas direções. Isso resulta em um único componente fortemente conexo que engloba toda a rede:

*   **Entrada:** Grafo de 7 vértices bidirecional.
*   **Componentes Fortemente Conexos:**
    *   `Componente 1: [7, 3, 5, 6, 4, 2, 1]`

## 💻 Exemplo de Uso em Python

```python
from algoritmos import tarjan_scc

graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

sccs = tarjan_scc(graph)
print(sccs)
# [[7, 3, 5, 6, 4, 2, 1]]
```
