# Verificação de Eulerianidade

Determina se o grafo possui circuito ou caminho euleriano. Para grafos não-direcionados conexos: todos os vértices com grau par → circuito euleriano; exatamente 2 com grau ímpar → caminho euleriano. Complexidade: **O(V + E)**.

---

## ▶️ Como Executar

```bash
python3 algoritmos/eulerian/eulerian.py
```

## 📋 Saída Esperada (Zachary's Karate Club)

```
Eulerianidade — Zachary's Karate Club
=============================================
Nós com grau ímpar: 12 → [1, 4, 8, 10, 11, 13, 19, 23, 24, 25, 28, 33]
Resultado: Não Euleriano

Explicação: como 12 > 2 nós têm grau ímpar, não existe
circuito nem caminho euleriano.
```

**Interpretação:** 12 dos 34 membros do clube possuem número ímpar de amizades. Isso é esperado em redes sociais reais — a eulerianidade exigiria uma estrutura muito artificial e simétrica, incompatível com relações humanas orgânicas.
