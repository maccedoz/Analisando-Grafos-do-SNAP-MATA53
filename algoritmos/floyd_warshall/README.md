# Algoritmo de Floyd-Warshall

Calcula os caminhos mínimos entre **todos os pares de vértices** usando programação dinâmica com três loops aninhados. Complexidade: **O(V³)**.

---

## ▶️ Como Executar

```bash
python3 algoritmos/floyd_warshall/floyd_warshall.py
```

## 📋 Saída Esperada (Zachary's Karate Club)

```
Floyd-Warshall — Zachary's Karate Club (todos os pares)
=======================================================
Amostra: caminhos mínimos a partir do nó 0:
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
  ... (34×34 = 1156 pares calculados)

Resultado: diâmetro ponderado do grafo = 11.0
```

**Interpretação:** Floyd-Warshall resolve todos os 1156 pares de nós de uma só vez. O diâmetro ponderado (11.0) é o maior caminho mínimo entre qualquer par — bem maior que o diâmetro topológico (5 saltos), pois os pesos adicionam custo às arestas. É o algoritmo mais lento do benchmark (~4959 µs), mas o único que entrega *todos os pares* simultaneamente.
