# Verificação de Eulerianidade

Este algoritmo determina se um grafo não direcionado conexo possui um **Circuito Euleriano** (todos os nós com grau par), um **Caminho Euleriano** (exatamente 2 nós com grau ímpar, também conhecido como Semi-Euleriano), ou se **Não é Euleriano**.

---

## 📈 Execução no Grafo do Artigo (SIGMOD 2026)

*   **Entrada:** Grafo de 7 vértices.
*   **Graus dos Vértices:**
    *   Vértice 1: Grau 2 (par)
    *   Vértice 2: Grau 3 (ímpar)
    *   Vértice 3: Grau 3 (ímpar)
    *   Vértice 4: Grau 3 (ímpar)
    *   Vértice 5: Grau 3 (ímpar)
    *   Vértice 6: Grau 1 (ímpar)
    *   Vértice 7: Grau 1 (ímpar)
*   **Resultado:** `"Não Euleriano"` (possui 6 vértices com grau ímpar, violando as condições necessárias).

## 💻 Exemplo de Uso em Python

```python
from algoritmos import is_eulerian

graph = {
    1: [2, 3],
    2: [1, 4, 3],
    3: [1, 5, 2],
    4: [2, 6, 5],
    5: [3, 4, 7],
    6: [4],
    7: [5]
}

resultado = is_eulerian(graph)
print(resultado) # "Não Euleriano"
```
