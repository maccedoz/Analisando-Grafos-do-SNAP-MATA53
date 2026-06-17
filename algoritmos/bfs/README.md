# Busca em Largura (BFS)

Algoritmo clássico de busca e exploração em grafos. Visita primeiro todos os vértices vizinhos imediatos (distância 1), depois os vizinhos destes (distância 2) e assim por diante.

---

## 📈 Execução no Grafo do Artigo (SIGMOD 2026)

Rodando a BFS a partir do vértice inicial `1`:

*   **Entrada:** Grafo de 7 vértices e vértice inicial `1`.
*   **Ordem de Visitação:** `[1, 2, 3, 4, 5, 6, 7]`

## 💻 Exemplo de Uso em Python

```python
from algoritmos import bfs

graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

resultado = bfs(graph, start=1)
print(resultado) # [1, 2, 3, 4, 5, 6, 7]
```
