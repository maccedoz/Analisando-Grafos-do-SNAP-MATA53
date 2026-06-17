# Algoritmo de Dijkstra

Calcula o caminho mínimo de uma origem para todos os outros nós em grafos com pesos não-negativos, usando uma fila de prioridade (heap binária). Complexidade: **O((V + E) log V)**.

---

## ▶️ Como Executar

```bash
python3 algoritmos/dijkstra/dijkstra.py
```

## 📋 Saída Esperada (Zachary's Karate Club, origem: nó 0)

```
Dijkstra — Zachary's Karate Club (origem: nó 0 / Mr. Hi)
=======================================================
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
  nó 12  →     3.0
  nó 13  →     4.0
  nó 14  →     7.0
  nó 15  →     8.0
  ... (34 nós no total)

Resultado: menor distância total = 1.0 (nó mais próximo: nó 5)
```

**Interpretação:** Os nós 5 e 10 são os vizinhos mais baratos de acessar a partir do nó 0 (distância 1.0). Os nós da facção do *Officer* (ex: nós 14, 15) têm distâncias maiores (7.0–8.0), refletindo a separação topológica entre as duas comunidades.
