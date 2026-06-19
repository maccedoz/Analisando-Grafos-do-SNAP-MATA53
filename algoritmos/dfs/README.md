# Busca em Profundidade (DFS)

Algoritmo de exploração que percorre o grafo o mais fundo possível antes de retroceder. Base para ordenação topológica e detecção de ciclos. Complexidade: **O(V + E)**.

---

## Como Executar

```bash
python3 algoritmos/dfs/dfs.py
```

## Saída Esperada (Zachary's Karate Club)

```
DFS — Zachary's Karate Club (nó inicial: 0 / Mr. Hi)
=======================================================
Nós visitados (34 no total):
  [0, 1, 2, 3, 7, 12, 13, 33, 8, 30, 32, 14, 15, 18, 20,
   22, 23, 25, 24, 27, 31, 28, 29, 26, 9, 19, 17, 21, 4,
   6, 5, 10, 16, 11]

Resultado: grafo totalmente conexo — todos os 34 nós
alcançados em profundidade a partir do nó 0.
```

**Interpretação:** A DFS mergulha pela facção de *Mr. Hi* antes de cruzar para a facção do *Officer* (nó 33 visitado no 8º passo), revelando a separação natural das duas comunidades.
