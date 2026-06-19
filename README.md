# Análise Estrutural e Algorítmica da Rede Zachary's Karate Club

> **Repositório GitHub:** [maccedoz/Analisando-Grafos-do-SNAP-MATA53](https://github.com/maccedoz/Analisando-Grafos-do-SNAP-MATA53.git)

Este repositório contém a implementação manual de algoritmos clássicos de Teoria dos Grafos, scripts de caracterização de redes complexas, benchmarks estatísticos de desempenho e um artigo científico completo em LaTeX. O trabalho analisa as propriedades estruturais da célebre rede social **Zachary's Karate Club**.

---

## Estrutura do Repositório

O projeto está organizado da seguinte forma:

*   **`algoritmos/`**: Pacote modular contendo as implementações manuais (do zero) de 8 algoritmos de grafos. Cada subpasta possui uma documentação (`README.md`) explicando sua complexidade e comportamento:
    1.  [bfs/](algoritmos/bfs/) (Busca em Largura)
    2.  [dfs/](algoritmos/dfs/) (Busca em Profundidade)
    3.  [eulerian/](algoritmos/eulerian/) (Verificação de Eulerianidade)
    4.  [dijkstra/](algoritmos/dijkstra/) (Algoritmo de Dijkstra para caminhos mínimos)
    5.  [bellman_ford/](algoritmos/bellman_ford/) (Algoritmo de Bellman-Ford com suporte a ciclos negativos)
    6.  [floyd_warshall/](algoritmos/floyd_warshall/) (Floyd-Warshall para todos os pares de caminhos mínimos)
    7.  [tarjan/](algoritmos/tarjan/) (Algoritmo de Tarjan para Componentes Fortemente Conexos)
    8.  [kruskal/](algoritmos/kruskal/) (Algoritmo de Kruskal para Árvore Geradora Mínima)
*   **`scripts/`**: Scripts Python para automação e execução:
    *   `gerar_dataset.py`: Trata a rede clássica, calcula pesos sintéticos deterministicamente e exporta no formato CSV.
    *   `gerar_graficos.py`: Produz a visualização do grafo e o histograma de distribuição de graus.
    *   `run_benchmarks.py`: Executa o benchmark estatístico dos algoritmos em 50 rodadas independentes com Intervalo de Confiança de 95%.
    *   `analise_estrutural.py`: Implementa do zero as métricas complexas (Small-world Humphries-Gurney, Lei de Potência log-log e simulações Monte Carlo de Robustez estrutural).
    *   `executar_algoritmos.py`: Menu interativo para executar cada algoritmo individualmente em modo detalhado (passo a passo) ou rodar todos consecutivamente.
*   **`data/`**: Base de dados tratada (`karate_club_edges.csv`).
*   **`graficos/`**: Imagens e plots gerados pelo projeto.
*   **`relatorio/`**: Artigo completo em LaTeX (`224116504.tex`) usando o formato de duas colunas `webmedia`.
*   **`artigos/`**: Literatura e publicações de referência.
*   **`venv/`**: Ambiente virtual Python contendo as dependências pré-instaladas.

---

## Como o Repositório Funciona (Guia de Execução)

Para garantir que todas as bibliotecas necessárias sejam encontradas e executadas sem erros, utilize o interpretador Python do ambiente virtual (`venv/bin/python3`) a partir do diretório raiz do projeto.

### 1. Configurando o Ambiente
Para ativar o ambiente virtual ou instalar os requisitos:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Rodando o Menu Interativo dos Algoritmos
O script de execução permite escolher interativamente qual algoritmo testar em tempo de execução, imprimindo o passo a passo simplificado com as explicações e caminhos detalhados em português:
```bash
venv/bin/python3 scripts/executar_algoritmos.py
```
*Selecione opções de `1` a `8` para acompanhar o comportamento passo a passo de um algoritmo específico, `9` para rodar todos sequencialmente de forma simplificada, ou `0` para sair.*

### 3. Gerando os Gráficos do Relatório
Gera a visualização circular do grafo (com nós numerados de 0 a 33 e cores indicando as facções) em `graficos/karate_club_graph.png`:
```bash
venv/bin/python3 scripts/gerar_graficos.py
```

### 4. Executando o Benchmark Estatístico
Executa a medição de tempo dos algoritmos sobre 50 rodadas e calcula a média, desvio padrão e o Intervalo de Confiança a 95% usando a distribuição Normal (Z):
```bash
venv/bin/python3 scripts/run_benchmarks.py
```

### 5. Executando a Análise Estrutural e Robustez
Calcula o índice Small-worldness ($\sigma_{sw}$), estima o expoente da lei de potência ($\gamma$) e realiza simulações Monte Carlo de remoção de 5% de nós (falha aleatória vs. ataque direcionado aos hubs):
```bash
venv/bin/python3 scripts/analise_estrutural.py
```

---

## Resumo dos Resultados Topológicos

*   **Topologia do Zachary's Karate Club**: 34 nós, 78 arestas, densidade de 13.9%, diâmetro geodésico de 5 saltos, comprimento de caminho médio de 2.408 saltos e coeficiente de clusterização médio de 0.571.
*   **Propriedade Small-World**: O coeficiente local de agrupamento é 4.4 vezes superior à sua contraparte aleatória de Erdős-Rényi, confirmando comportamento acentuado de pequeno mundo ($\sigma_{sw} \approx 4.39$).
*   **Robustez e Vulnerabilidade**: Sob 5% de falhas aleatórias a rede é extremamente tolerante. Contudo, sob ataque direcionado aos dois maiores hubs (nós 0 e 33), a rede fragmenta-se fisicamente em 3 componentes isolados. Este resultado matemático prediz a cisão social real sofrida historicamente pelo clube.
