# Algoritmo de Bellman-Ford

Calcula o caminho mínimo de uma origem para todos os nós, suportando pesos negativos e detectando ciclos de peso negativo. Opera relaxando todas as arestas V−1 vezes. Complexidade: **O(V · E)**.

---

## Como Executar

```bash
python3 algoritmos/bellman_ford/bellman_ford.py
```

## Saída Esperada (Zachary's Karate Club, origem: nó 0)

```
Bellman-Ford — Zachary's Karate Club (origem: nó 0 / Mr. Hi)
============================================================
 Destino  Dist. Mínima
-------------------------
  nó  0  →     0.0
  nó  1  →     2.0
  nó  2  →     3.0
  nó  3  →     4.0
  nó  4  →     3.0
  nó  5  →     1.0
  nó  6  →     2.0
  nó  7  →     3.0
  nó  8  →     4.0
  nó  9  →     5.0
  nó 10  →     1.0
  nó 11  →     2.0
  nó 13  →     4.0
  nó 14  →     7.0
  nó 15  →     8.0
  ... (34 nós no total)

Resultado: sem ciclos negativos. Caminhos mínimos idênticos ao Dijkstra.
```

**Interpretação:** Os resultados são idênticos ao Dijkstra (todos os pesos são positivos). O Bellman-Ford é ~17× mais lento neste grafo (695 µs vs 40 µs), pois relaxa as 78 arestas 33 vezes = 2574 operações, contra a abordagem gulosa do Dijkstra.
