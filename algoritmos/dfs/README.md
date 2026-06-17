# Busca em Profundidade (DFS)

Algoritmo clássico de busca e exploração em grafos. Explora o grafo percorrendo caminhos de forma recursiva até atingir vértices sem vizinhos não visitados, retrocedendo em seguida.

---

## 📈 Execução no Grafo Zachary's Karate Club

Rodando a DFS a partir do vértice inicial `1`:

*   **Entrada:** Grafo de 7 vértices e vértice inicial `1`.
*   **Ordem de Visitação:** `[1, 2, 4, 6, 5, 3, 7]`

## 💻 Exemplo de Uso em Python

```python
from algoritmos import dfs

graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

resultado = dfs(graph, start=1)
print(resultado) # [1, 2, 4, 6, 5, 3, 7]
```
