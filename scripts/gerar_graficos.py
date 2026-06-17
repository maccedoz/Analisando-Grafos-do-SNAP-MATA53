import os
import sys
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
graficos_dir = os.path.join(base_dir, "graficos")
os.makedirs(graficos_dir, exist_ok=True)

# Carregar o grafo Zachary's Karate Club
G = nx.karate_club_graph()

# 1. Gráfico da Estrutura do Grafo (Layout Circular Original do Artigo de Zachary)
plt.figure(figsize=(7.5, 7.5), dpi=300)
plt.style.use('default')

# Determinar cores com base nas facções (Mr. Hi e John A.)
colors = []
for n, data in G.nodes(data=True):
    if data['club'] == 'Mr. Hi':
        colors.append('#2563EB') # Azul Royal elegante
    else:
        colors.append('#DC2626') # Vermelho elegante

# Posicionamento circular idêntico ao artigo original:
# Nós 1 a 34 dispostos no sentido horário, com 34 e 1 centralizados simetricamente no topo.
pos = {}
num_nodes = len(G.nodes())
theta = 2 * np.pi / num_nodes

for u in G.nodes():
    k = u + 1 # Identificador do nó (1-based, conforme artigo original)
    alpha = np.pi/2 - (k - 0.5) * theta
    pos[u] = np.array([np.cos(alpha), np.sin(alpha)])

# Desenhar arestas (linhas pretas finas e limpas)
nx.draw_networkx_edges(G, pos, alpha=0.7, edge_color='#1E293B', width=0.7)

# Desenhar nós (círculos coloridos azul/vermelho)
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=150, edgecolors='#000000', linewidths=0.8)

# Desenhar rótulos externos de 1 a 34
for u in G.nodes():
    x, y = pos[u]
    # Deslocamento radial externo para o rótulo
    label_offset = 0.12
    label_x = x * (1 + label_offset)
    label_y = y * (1 + label_offset)
    
    label_text = str(u + 1)
    
    plt.text(label_x, label_y, label_text, 
             ha='center', va='center', 
             fontsize=9, fontweight='bold', color='black',
             fontfamily='sans-serif')

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(graficos_dir, 'karate_club_graph.png'), facecolor='white', edgecolor='none', bbox_inches='tight')
plt.close()

# 2. Gráfico da Distribuição de Graus
plt.figure(figsize=(8, 5), dpi=300)
plt.style.use('dark_background')

degrees = [d for n, d in G.degree()]
unique_degrees, counts = np.unique(degrees, return_counts=True)

# Criar gráfico de barras
bars = plt.bar(unique_degrees, counts, color='#10B981', edgecolor='white', width=0.6, alpha=0.85)

# Adicionar rótulos nas barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.15, str(yval), 
             ha='center', va='bottom', fontsize=9, color='white', fontweight='bold')

plt.title("Distribuição de Graus (Degree Distribution)", fontsize=14, fontweight='bold', color='white', pad=15)
plt.xlabel("Grau (k)", fontsize=11, color='white', labelpad=10)
plt.ylabel("Frequência (Quantidade de Nós)", fontsize=11, color='white', labelpad=10)
plt.xticks(np.arange(1, 19, 1))
plt.yticks(np.arange(0, 13, 2))
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('#475569')
plt.gca().spines['bottom'].set_color('#475569')

plt.tight_layout()
plt.savefig(os.path.join(graficos_dir, 'karate_club_degree_distribution.png'), facecolor='#0F172A', edgecolor='none')
plt.close()

print("Gráficos gerados com sucesso!")
