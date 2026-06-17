# Análise Estrutural e Algorítmica da Rede Zachary's Karate Club

> 📦 **Repositório GitHub:** [maccedoz/Analisando-Grafos-do-SNAP-MATA53](https://github.com/maccedoz/Analisando-Grafos-do-SNAP-MATA53.git)

Este repositório contém o código-fonte, scripts de análise de desempenho e o conjunto de dados tratados para o estudo topológico e algorítmico da célebre rede social **Zachary's Karate Club**. O trabalho foi desenvolvido como requisito avaliativo para a disciplina de Teoria dos Grafos da Universidade Federal de Lavras (UFLA).

---

## 📁 Estrutura do Repositório

O projeto está estruturado em pastas organizadas por finalidade:

*   **`algoritmos/`**: Pacote Python contendo as implementações manuais (do zero) de 8 algoritmos clássicos de grafos. Cada algoritmo possui sua própria pasta e documentação dedicada:
    1.  [bfs/](algoritmos/bfs/) ([README](algoritmos/bfs/README.md)): Busca em Largura (BFS)
    2.  [dfs/](algoritmos/dfs/) ([README](algoritmos/dfs/README.md)): Busca em Profundidade (DFS)
    3.  [eulerian/](algoritmos/eulerian/) ([README](algoritmos/eulerian/README.md)): Verificação de Eulerianidade
    4.  [dijkstra/](algoritmos/dijkstra/) ([README](algoritmos/dijkstra/README.md)): Algoritmo de Dijkstra
    5.  [bellman_ford/](algoritmos/bellman_ford/) ([README](algoritmos/bellman_ford/README.md)): Algoritmo de Bellman-Ford
    6.  [floyd_warshall/](algoritmos/floyd_warshall/) ([README](algoritmos/floyd_warshall/README.md)): Algoritmo de Floyd-Warshall
    7.  [tarjan/](algoritmos/tarjan/) ([README](algoritmos/tarjan/README.md)): Algoritmo de Tarjan (SCC)
    8.  [kruskal/](algoritmos/kruskal/) ([README](algoritmos/kruskal/README.md)): Algoritmo de Kruskal (MST)
    *   *Consulte o [algoritmos/README.md](algoritmos/README.md) do pacote geral para uma visão integrada.*
*   **`scripts/`**: Scripts de automação, análise e simulação:
    *   `gerar_dataset.py`: Exporta o grafo clássico do NetworkX para o formato CSV estruturado.
    *   `gerar_graficos.py`: Gera os gráficos em alta definição para o relatório.
    *   `run_benchmarks.py`: Executa o benchmark de tempo de execução com 50 rodadas e Intervalo de Confiança a 95%.
    *   `analise_estrutural.py`: Roda a análise estrutural avançada (Small-world, Lei de Potência, Robustez).
    *   `executar_algoritmos.py`: Script de teste rápido que executa os 8 algoritmos sobre o grafo do artigo de referência (SIGMOD 2026).
    *   `script.py`: ~~removido~~ (era simulador de outro projeto, não relacionado ao Karate Club)
*   **`data/`**: Pasta para o conjunto de dados estruturado:
    *   `karate_club_edges.csv`: Lista de adjacência tratada contendo arestas, pesos normalizados e facções dos nós.
*   **`graficos/`**: Pasta de saída para as visualizações geradas:
    *   `karate_club_graph.png`: Visualização do grafo com nós coloridos conforme a facção.
    *   `karate_club_degree_distribution.png`: Distribuição de frequências por grau de nós.
*   **`relatorio/`**: Arquivos do artigo científico científico completo:
    *   `relatorio.tex`: Relatório científico em LaTeX estruturado segundo a classe `webmedia`.
    *   `sample-base.bib`: Banco de referências BibTeX.
*   **`artigos/`**: Artigos científicos e referências em texto associados ao projeto.

---

## 🛠️ Pré-requisitos e Execução

### Instalação das Bibliotecas
Os scripts utilizam a versão padrão do Python 3 e exigem as seguintes bibliotecas:
```bash
pip install -r requirements.txt
```

### Como Executar os Scripts

Todos os comandos devem ser rodados a partir do diretório raiz do projeto:

1.  **Gerar o Dataset Tratado (`data/karate_club_edges.csv`)**:
    ```bash
    python3 scripts/gerar_dataset.py
    ```
2.  **Gerar as Visualizações e Gráficos (`graficos/`)**:
    ```bash
    python3 scripts/gerar_graficos.py
    ```
3.  **Executar a Medição Temporal dos Algoritmos (Benchmark)**:
    ```bash
    python3 scripts/run_benchmarks.py
    ```
4.  **Executar a Análise de Pequeno Mundo, Lei de Potência e Robustez**:
    ```bash
    python3 scripts/analise_estrutural.py
    ```
5.  **Rodar a Demonstração de Todos os Algoritmos (Grafo do Artigo Analisado)**:
    ```bash
    python3 scripts/executar_algoritmos.py
    ```
6.  **Configurar o Ambiente Rapidamente**:
    ```bash
    ./dev.sh
    ```

---

## 📊 Resumo dos Resultados Obtidos

*   **Propriedades Básicas**: A rede é totalmente conexa (1 componente de tamanho 34), possui 78 arestas, densidade de 13,9%, diâmetro igual a 5, raio igual a 3, comprimento médio dos caminhos de 2,408 saltos e coeficiente de clusterização de 0,571.
*   **Small-World**: Índice sigma_sw ≈ 4,39 > 1. O grafo apresenta comportamento acentuado de pequeno mundo (clusterização local alta com caminhos curtos).
*   **Lei de Potência**: O expoente estimado é de gamma ≈ 0,55. O grafo não segue uma lei de potência pura devido ao seu tamanho reduzido (N=34), mas sua distribuição é assimétrica e governada por hubs.
*   **Robustez**:
    *   *Falha Aleatória (5% dos nós)*: O grafo se mantém conexo com tamanho médio do LCC de 31,55 (de 32) e caminhos de 2,41 saltos.
    *   *Ataque Direcionado (5% mais centrais)*: A remoção dos hubs 0 e 33 fratura a rede em 3 componentes isolados.
*   **Descoberta Sociológica**: A análise de ataque direcionado prediz matematicamente a cisão social real do clube de caratê descrita historicamente por Zachary.
