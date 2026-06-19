# Algoritmo de Tarjan (SCC)

Identifica Componentes Fortemente Conexos (SCCs) em grafos direcionados usando uma única varredura DFS com pilha e índices de baixo-link. Complexidade: **O(V + E)**.

---

## Como Executar

```bash
python3 algoritmos/tarjan/tarjan.py
```

## Saída Esperada (Zachary's Karate Club)

```
Tarjan SCC — Zachary's Karate Club
=============================================
Componentes Fortemente Conexos encontrados: 1
  SCC 1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
          14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
          26, 27, 28, 29, 30, 31, 32, 33]  (tamanho: 34)

Resultado: 1 componente(s) — a rede é totalmente conexa.
```

**Interpretação:** Como o grafo é não-direcionado, as arestas foram tratadas como bidirecionais, resultando em um único SCC contendo todos os 34 membros. Isso confirma a conectividade total da rede — todos os membros estavam integrados *antes* da cisão.
