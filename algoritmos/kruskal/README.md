# Algoritmo de Kruskal (MST)

Constrói a Árvore Geradora Mínima (MST) ordenando as arestas por peso e usando uma estrutura Union-Find (DSU) com compressão de caminhos para evitar ciclos. Complexidade: **O(E log V)**.

---

## ▶️ Como Executar

```bash
python3 algoritmos/kruskal/kruskal.py
```

## 📋 Saída Esperada (Zachary's Karate Club)

```
Kruskal MST — Zachary's Karate Club
=============================================
Arestas na MST (33 = N-1 = 34-1):
  ( 0 —  5)  peso: 1.0
  ( 0 — 10)  peso: 1.0
  ( 1 — 19)  peso: 1.0
  ( 2 —  3)  peso: 1.0
  ( 2 —  8)  peso: 1.0
  ( 2 — 13)  peso: 1.0
  ( 2 — 28)  peso: 1.0
  ( 3 —  7)  peso: 1.0
  ( 3 — 12)  peso: 1.0
  ( 4 —  6)  peso: 1.0
  ( 8 — 32)  peso: 1.0
  ( 8 — 33)  peso: 1.0   ← ponte entre facções!
  ...
  (todas 33 arestas)

Resultado: Peso total da MST = 51.0
```

**Interpretação:** A MST conecta todos os 34 membros com o menor custo total de 51.0 usando exatamente 33 arestas (N−1). As arestas de peso 1.0 (mais baratas) são priorizadas. A aresta (8 — 33) é particularmente interessante: é uma das pontes entre a facção de *Mr. Hi* e a do *Officer* que aparece na MST, revelando o elo mais econômico entre os dois grupos.
