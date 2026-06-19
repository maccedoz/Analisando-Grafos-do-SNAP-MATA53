# Busca em Largura (BFS)

Algoritmo clássico de busca e exploração em grafos. Visita primeiro todos os vizinhos imediatos (distância 1), depois os vizinhos destes (distância 2) e assim por diante. Complexidade: **O(V + E)**.

---

## Como Executar

```bash
python3 algoritmos/bfs/bfs.py
```

## Saída Esperada (Zachary's Karate Club)

```
BFS — Zachary's Karate Club (nó inicial: 0 / Mr. Hi)
=======================================================
Nós visitados (34 no total):
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 17, 19, 21,
   31, 30, 9, 27, 28, 32, 16, 33, 24, 25, 23, 14, 15, 18,
   20, 22, 29, 26]

Resultado: grafo totalmente conexo — todos os 34 nós
alcançados a partir do nó 0.
```

**Interpretação:** O nó 0 (Mr. Hi) alcança diretamente 16 vizinhos. A partir deles, em 2 saltos, toda a rede é coberta — evidência da propriedade *small-world* (comprimento médio de caminhos ≈ 2,4 saltos).
