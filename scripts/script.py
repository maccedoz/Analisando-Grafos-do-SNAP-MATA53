import os
import sys
# Adicionar o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import heapq

# ──────────────────────────────────────────────
# DADOS E GRAFO EXEMPLO
# ──────────────────────────────────────────────
@st.cache_resource
def carregar_grafo():
    G = nx.Graph()
    G.add_weighted_edges_from([
        (1, 2, 2), (1, 3, 5),
        (2, 4, 1), (2, 3, 2),
        (3, 5, 3), (4, 6, 4),
        (4, 5, 2), (5, 7, 1),
    ])
    # Posições para visualização do Grafo Original
    pos = {1:(0.0,1.5), 2:(1.5,2.5), 3:(1.5,0.5),
           4:(3.0,2.5), 5:(3.0,0.5), 6:(4.5,2.5), 7:(4.5,0.5)}
    return G, pos

G, pos = carregar_grafo()

OBJETOS    = {3, 5, 6, 7}          # Veículos/entregadores na rede
PRED_Q     = [1, 2, 4, 5]          # Predecessores de q=1 na Árvore de Corte (caminho no artigo)
DIST_PRED  = {1:0, 2:2, 4:3, 5:5}  # lsd(c, q=1) — distância real de q até cada predecessor
INDICE     = {                     # M_k^≥(c): lista (lsd_c_o, objeto), ordem crescente
    1: [(4,3),(5,5),(6,7),(7,6)],
    2: [(2,3),(3,5),(4,7),(5,6)],
    4: [(2,5),(3,7),(3,3),(4,6)],
    5: [(0,5),(1,7),(3,3),(6,6)],
}

PSEUDOCODIGO = [
    ("1",  "Mk(q) ← ∅  ;  Q ← Min-Heap vazia"),
    ("2",  "Para cada predecessor c em P(q):"),
    ("3",  "    Se M_k^≥(c) não for vazio:"),
    ("4",  "        Inserir (lsd(c,q) + lsd(c, 1°obj), c, 1°obj, idx=0) em Q"),
    ("5",  "Enquanto |Mk| < k  E  Q não vazia:"),
    ("6",  "    (d, c, o, idx) ← Desempilhar topo de Q"),
    ("7",  "    Se o ∉ Mk(q): adicionar o a Mk(q)"),
    ("8",  "    Se |Mk| < k  E  existe próximo em lista local de c:"),
    ("9",  "        Inserir próximo objeto de c em Q"),
    ("10", "Retornar Mk(q)"),
]

# Layout e nós da árvore de decomposição de cortes de vértices (CtLd-Cons) com C = {2, 4, 5}
POS_TREE_DECOMP = {
    "A": (0.0, 1.0),
    "B": (-1.2, 0.0),
    "C": (1.2, 0.0)
}

LABELS_TREE_DECOMP = {
    "A": "{2, 4, 5}",
    "B": "{1, 3}",
    "C": "{6, 7}"
}

ALL_TREE_EDGES = [("A", "B"), ("A", "C")]

# Dados dos Passos do Algoritmo CtLd-Cons para criar a Árvore de Decomposição
PASSOS_ARVORE = [
    {
        "passo": 0,
        "titulo": "Estado Inicial (Árvore Vazia)",
        "cut_nodes": set(),
        "L_nodes": set(),
        "R_nodes": set(),
        "tree_nodes_active": set(),
        "tree_edges_active": set(),
        "narrativa": "Inicialização do algoritmo <b>CtLd-Cons</b> (Algoritmo 1 do artigo). Temos o grafo original completo de 7 vértices e a árvore de corte ainda vazia. O algoritmo funciona identificando recursivamente <b>cortes de vértices balanceados</b> (separadores de vértices) para decompor o grafo em componentes menores."
    },
    {
        "passo": 1,
        "titulo": "Corte 1: Separador Global C = {2, 4, 5}",
        "cut_nodes": {2, 4, 5},
        "L_nodes": {1, 3},
        "R_nodes": {6, 7},
        "tree_nodes_active": {"A"},
        "tree_edges_active": set(),
        "narrativa": "O algoritmo executa a função <b>BalancedCut</b> no grafo original. O separador de vértices encontrado é <b>C = {2, 4, 5}</b> (destacado em laranja). Remover estes três vértices desconecta completamente o grafo, eliminando a aresta 3-5 que ligava os dois lados. O grafo fica dividido em: <b>L = {1, 3}</b> (azul, esquerda) e <b>R = {6, 7}</b> (vermelho, direita). O nó contendo {2, 4, 5} é inserido como a raiz da árvore."
    },
    {
        "passo": 2,
        "titulo": "Recursão à Esquerda: g[L] com L = {1, 3}",
        "cut_nodes": set(),
        "L_nodes": {1, 3},
        "R_nodes": set(),
        "tree_nodes_active": {"A", "B"},
        "tree_edges_active": {("A", "B")},
        "narrativa": "O algoritmo realiza a chamada recursiva para o subgrafo esquerdo contendo <b>{1, 3}</b>. Como este subgrafo possui apenas 2 vértices (<b>|L| ≤ 2</b>), a recursão atinge o caso base e cria um nó folha contendo <b>{1, 3}</b>, conectando-o diretamente como filho esquerdo da raiz {2, 4, 5}."
    },
    {
        "passo": 3,
        "titulo": "Recursão à Direita: g[R] com R = {6, 7}",
        "cut_nodes": set(),
        "L_nodes": set(),
        "R_nodes": {6, 7},
        "tree_nodes_active": {"A", "B", "C"},
        "tree_edges_active": {("A", "B"), ("A", "C")},
        "narrativa": "O algoritmo realiza a chamada recursiva para o subgrafo direito contendo <b>{6, 7}</b>. Como este subgrafo possui apenas 2 vértices (<b>|R| ≤ 2</b>), a recursão atinge o caso base e cria um nó folha contendo <b>{6, 7}</b>, conectando-o como filho direito da raiz {2, 4, 5}."
    },
    {
        "passo": 4,
        "titulo": "Árvore de Decomposição Concluída!",
        "cut_nodes": set(),
        "L_nodes": set(),
        "R_nodes": set(),
        "tree_nodes_active": {"A", "B", "C"},
        "tree_edges_active": {("A", "B"), ("A", "C")},
        "destacar_predecessores": True,
        "narrativa": "<b>Árvore de Decomposição de Vértices Concluída!</b><br><br>Pela lógica de busca do artigo, para qualquer vértice de consulta <i>q</i>, seus predecessores <b>P(q)</b> são compostos por ele mesmo mais os vértices contidos nos nós <b>ancestrais</b> da árvore de corte.<br>Para <b>q = 1</b> (que reside no nó folha {1, 3}), o único nó ancestral é a raiz <b>{2, 4, 5}</b>.<br>Logo, os predecessores são exatamente <b>{1, 2, 4, 5}</b> (destacados no grafo e na árvore). Isso justifica por que esses nós são usados como predecessores na busca kNN da Aba 2!"
    }
]

# ──────────────────────────────────────────────
# ESTADOS DO SIMULADOR
# ──────────────────────────────────────────────
def reset_knn():
    st.session_state.update(
        iniciado=False, Q=[], Mk=[], Mk_set=set(),
        passo=0, terminado=False,
        linha_ativa=None,
        narrativa="",
        ultimo_pop=None,
        foi_duplicata=False,
        historico=[],
    )

def reset_tree():
    st.session_state.update(
        tree_passo=0,
        tree_iniciado=True
    )

if "iniciado" not in st.session_state:
    reset_knn()

if "tree_passo" not in st.session_state or st.session_state.tree_passo < 0 or st.session_state.tree_passo >= len(PASSOS_ARVORE):
    reset_tree()

if "pred_q_check" not in st.session_state or st.session_state.pred_q_check != PRED_Q:
    st.session_state.pred_q_check = PRED_Q
    reset_knn()
    reset_tree()


# ──────────────────────────────────────────────
# PÁGINA E CONTROLES (SIDEBAR DINEGÓCIOS)
# ──────────────────────────────────────────────
st.set_page_config(layout="wide", page_title="Simulador CTLD & Gomory-Hu")
st.title("Simulador de Redes Viárias: Gomory-Hu & CTLD-Query")
st.caption(
    "Artigo de Base: *High-Throughput k Nearest Neighbors Search in Road Networks* — SIGMOD 2026  |  "
    "Escolha a etapa de simulação na barra lateral."
)

with st.sidebar:
    st.header("Navegação")
    modo = st.radio(
        "Selecione a Etapa",
        ["1. Criação da Árvore de Corte", "2. Busca kNN (CTLD-Query)"]
    )
    
    st.divider()
    
    if modo == "1. Criação da Árvore de Corte":
        st.subheader("Controles da Árvore")
        st.info("Aqui simulamos o algoritmo de Gusfield para construir a árvore de corte (Gomory-Hu) do nosso grafo.")
        
        c1, c2, c3 = st.columns(3)
        if c1.button("Reiniciar", key="btn_tree_reset"):
            reset_tree()
        
        pode_avancar = st.session_state.tree_passo < len(PASSOS_ARVORE) - 1
        pode_voltar = st.session_state.tree_passo > 0
        
        if c2.button("Voltar", key="btn_tree_prev", disabled=not pode_voltar):
            st.session_state.tree_passo -= 1
            
        if c3.button("Avançar", key="btn_tree_next", disabled=not pode_avancar):
            st.session_state.tree_passo += 1
            
        st.metric("Passo Atual", f"{st.session_state.tree_passo} / {len(PASSOS_ARVORE) - 1}")
        
    else:
        st.subheader("Controles do kNN")
        st.info("**Ponto de consulta fixo:** nó q = 1")
        k = st.slider("k — quantos vizinhos buscar?", 1, 4, 2, key="k_slider")
        
        c1, c2 = st.columns(2)
        if c1.button("Iniciar", key="btn_knn_init"):
            reset_knn()
            fila = []
            linhas_init = []
            for c in PRED_Q:
                lst = INDICE.get(c, [])
                if lst:
                    lsd_co, o = lst[0]
                    d = DIST_PRED[c] + lsd_co
                    heapq.heappush(fila, (d, c, o, 0))
                    linhas_init.append(
                        f"c={c}: push obj **{o}**  →  "
                        f"dist = lsd({c},q)+lsd({c},{o}) = {DIST_PRED[c]}+{lsd_co} = **{d}**"
                    )
            st.session_state.Q       = fila
            st.session_state.iniciado = True
            st.session_state.linha_ativa = "2-4"
            st.session_state.narrativa = (
                "**Inicialização concluída.** O algoritmo percorreu cada predecessor "
                f"c ∈ P(q) = {PRED_Q} e inseriu o **primeiro** objeto de cada lista local "
                "na fila de prioridade Q, usando a distância total = dist(q→c) + dist(c→objeto). "
                "Agora Q contém os melhores candidatos iniciais de cada predecessor."
            )
            st.session_state.historico = [{"passo": "INIT", "linhas": linhas_init}]
            
        pode_knn_avancar = (
            st.session_state.iniciado
            and not st.session_state.terminado
            and len(st.session_state.Mk) < k
            and len(st.session_state.Q) > 0
        )
        if c2.button("Avançar", key="btn_knn_next", disabled=not pode_knn_avancar):
            st.session_state.passo += 1
            p = st.session_state.passo
            
            d, c, o, idx = heapq.heappop(st.session_state.Q)
            st.session_state.ultimo_pop = (d, c, o, idx)
            st.session_state.linha_ativa = "6"
            
            linhas_passo = [f"Pop: dist={d}, obj={o}, via c={c}"]
            foi_dup = o in st.session_state.Mk_set
            
            if not foi_dup:
                st.session_state.Mk.append(o)
                st.session_state.Mk_set.add(o)
                acao = f"[+] **obj {o} adicionado** → Mk = {st.session_state.Mk}"
                st.session_state.narrativa = (
                    f"**Passo {p} — Novo vizinho encontrado!**  \n"
                    f"O topo da fila era o objeto **{o}** com distância total **{d}** "
                    f"(chegou via predecessor c={c}).  \n"
                    f"Como **{o} ainda não estava em Mk**, foi adicionado.  \n"
                    f"Resultado atual: **Mk = {st.session_state.Mk}** ({len(st.session_state.Mk)}/{k} vizinhos)."
                )
            else:
                acao = f"[!] **obj {o} duplicata** — descartado. Mk = {st.session_state.Mk}"
                st.session_state.narrativa = (
                    f"**Passo {p} — Duplicata descartada.**  \n"
                    f"O topo da fila era o objeto **{o}** com distância total **{d}** "
                    f"(chegou via predecessor c={c}).  \n"
                    f"**{o} já estava em Mk** — chegou por um caminho mais longo. "
                    "O algoritmo descarta e avança a fronteira desse predecessor.  \n"
                    f"Mk segue: **{st.session_state.Mk}**."
                )
                
            st.session_state.foi_duplicata = foi_dup
            linhas_passo.append(acao)
            
            if len(st.session_state.Mk) < k:
                lst_c = INDICE.get(c, [])
                nxt = idx + 1
                if nxt < len(lst_c):
                    lsd_next, o_next = lst_c[nxt]
                    d_next = DIST_PRED[c] + lsd_next
                    heapq.heappush(st.session_state.Q, (d_next, c, o_next, nxt))
                    linhas_passo.append(
                        f"Push próximo de c={c}: obj **{o_next}**  →  "
                        f"dist = {DIST_PRED[c]}+{lsd_next} = **{d_next}**"
                    )
                else:
                    linhas_passo.append(f"Lista de c={c} esgotada, nada a inserir.")
                    
            st.session_state.historico.append({"passo": p, "linhas": linhas_passo})
            
            if len(st.session_state.Mk) >= k:
                st.session_state.terminado = True
                st.session_state.linha_ativa = "10"
            elif not st.session_state.Q:
                st.session_state.terminado = True
                st.session_state.linha_ativa = "10"

        st.divider()
        st.subheader("Status do kNN")
        st.metric("Passos kNN", st.session_state.passo)
        prog = len(st.session_state.Mk)
        st.metric("Vizinhos encontrados", f"{prog} / {k}")
        st.progress(prog / k if k else 0)
        if st.session_state.terminado:
            st.success("Busca Concluída!")
        elif st.session_state.iniciado:
            st.info("Aguardando próximo passo")
        else:
            st.warning("Não iniciado")

# ──────────────────────────────────────────────
# TELA PRINCIPAL - MODO 1: CONSTRUÇÃO DA ÁRVORE DE CORTE
# ──────────────────────────────────────────────
if modo == "1. Criação da Árvore de Corte":
    st.subheader("Como a Árvore de Decomposição (Cortes de Vértices) é Gerada")
    st.markdown(
        "A árvore de corte (decomposição de vértices) é gerada por meio de uma decomposição recursiva "
        "baseada em **separadores de vértices balanceados** (Balanced Cuts), seguindo o algoritmo **CtLd-Cons** do artigo (Página 10)."
    )
    
    # Acesso seguro limitando o índice aos limites válidos da lista
    idx_passo = max(0, min(st.session_state.tree_passo, len(PASSOS_ARVORE) - 1))
    passo_info = PASSOS_ARVORE[idx_passo]
    
    col_g_tree, col_a_tree = st.columns([1, 1])
    
    with col_g_tree:
        st.subheader("Grafo Original e Partições")
        if passo_info.get("destacar_predecessores"):
            st.caption("Vermelho = q=1 (consulta) | Roxo = Predecessores {2, 4, 5} | Cinza = Demais nós")
        else:
            st.caption("Laranja = Separador de Vértices C | Azul = Partição L (Esquerda) | Vermelho = Partição R (Direita) | Cinza = Fora de escopo")
        
        # Colorir nós do grafo conforme partição do CtLd-Cons
        node_colors = []
        node_sizes = []
        for n in G.nodes():
            if passo_info.get("destacar_predecessores"):
                if n == 1:
                    node_colors.append("#EF4444") # vermelho para q=1
                    node_sizes.append(850)
                elif n in {2, 4, 5}:
                    node_colors.append("#A78BFA") # roxo para predecessores
                    node_sizes.append(800)
                else:
                    node_colors.append("#475569") # cinza
                    node_sizes.append(650)
            else:
                if passo_info["passo"] == 0:
                    node_colors.append("#64748B") # cinza padrão inicial
                    node_sizes.append(650)
                elif n in passo_info["cut_nodes"]:
                    node_colors.append("#F59E0B") # laranja
                    node_sizes.append(850)
                elif n in passo_info["L_nodes"]:
                    node_colors.append("#3B82F6") # azul
                    node_sizes.append(750)
                elif n in passo_info["R_nodes"]:
                    node_colors.append("#EF4444") # vermelho
                    node_sizes.append(750)
                else:
                    node_colors.append("#334155") # cinza escuro para fora de escopo
                    node_sizes.append(550)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor("#0F172A")
        ax.set_facecolor("#0F172A")
        
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes,
                               ax=ax, edgecolors="white", linewidths=1.5)
        nx.draw_networkx_edges(G, pos, width=2.0, edge_color="#475569", alpha=0.85, ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=11, font_color="white", font_weight="bold", ax=ax)
        
        # Desenhar rótulos dos pesos nas arestas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,"weight"),
                                     font_size=9, font_color="#CBD5E1", ax=ax,
                                     bbox=dict(boxstyle="round,pad=0.2", fc="#1E293B", alpha=0.8))
        
        plt.axis("off")
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)
        
    with col_a_tree:
        st.subheader("Árvore de Decomposição de Cortes")
        st.caption("Círculos coloridos são nós da árvore ativos. Linhas sólidas azuis representam as subdivisões já mapeadas pelo algoritmo.")
        
        # Criar grafo para visualização da árvore
        T = nx.DiGraph()
        for node in POS_TREE_DECOMP.keys():
            T.add_node(node)
        for u, v in ALL_TREE_EDGES:
            T.add_edge(u, v)
            
        # Determinar cores dos nós da árvore
        tree_node_colors = []
        for n in T.nodes():
            if n in passo_info["tree_nodes_active"]:
                if passo_info.get("destacar_predecessores") and n in {"A", "B"}:
                    tree_node_colors.append("#A78BFA") # Roxo para os nós predecessores de q=1
                else:
                    tree_node_colors.append("#10B981") # Verde ativo
            else:
                tree_node_colors.append("#1E293B") # Cinza inativo
                
        # Determinar estilo e cores das arestas da árvore
        tree_edge_colors = []
        tree_edge_styles = []
        tree_edge_widths = []
        for u, v in T.edges():
            if (u, v) in passo_info["tree_edges_active"]:
                tree_edge_colors.append("#3B82F6") # azul
                tree_edge_styles.append("solid")
                tree_edge_widths.append(2.5)
            else:
                tree_edge_colors.append("#334155") # cinza
                tree_edge_styles.append("dashed")
                tree_edge_widths.append(1.2)
                
        fig_t, ax_t = plt.subplots(figsize=(6, 4))
        fig_t.patch.set_facecolor("#0F172A")
        ax_t.set_facecolor("#0F172A")
        
        # Nós maiores para acomodar o texto dos conjuntos de vértices (ex: "{2, 4}")
        nx.draw_networkx_nodes(T, POS_TREE_DECOMP, node_color=tree_node_colors, node_size=1500,
                               ax=ax_t, edgecolors="#475569", linewidths=1.5)
        
        # Rótulos dos nós com o nome dos conjuntos correspondentes
        nx.draw_networkx_labels(T, POS_TREE_DECOMP, labels=LABELS_TREE_DECOMP,
                                font_size=9, font_color="white", font_weight="bold", ax=ax_t)
        
        # Desenhar as arestas com o estilo correspondente
        for idx, (u, v) in enumerate(T.edges()):
            nx.draw_networkx_edges(T, POS_TREE_DECOMP, edgelist=[(u, v)],
                                   width=tree_edge_widths[idx],
                                   edge_color=tree_edge_colors[idx],
                                   style=tree_edge_styles[idx],
                                   arrowstyle="->", arrowsize=15, ax=ax_t)
                                   
        plt.axis("off")
        plt.tight_layout()
        st.pyplot(fig_t)
        plt.close(fig_t)
        
    st.divider()
    
    st.subheader(f"Explicação: {passo_info['titulo']}")
    st.markdown(
        f"<div style='background:#1E293B; border-left:4px solid #3B82F6; border-radius:8px; padding:15px; font-size:1.0rem; color:#E2E8F0; line-height:1.6'>"
        f"{passo_info['narrativa']}"
        f"</div>",
        unsafe_allow_html=True
    )

# ──────────────────────────────────────────────
# TELA PRINCIPAL - MODO 2: BUSCA KNN
# ──────────────────────────────────────────────
else:
    col_grafo, col_algo, col_fila = st.columns([2, 1.4, 1.6])
    
    # ── COLUNA 1 — GRAFO ORIGINAL E KNN ──
    with col_grafo:
        st.subheader("Rede Viária")
        
        em_fila_set  = {item[2] for item in st.session_state.Q}
        Mk_set       = st.session_state.Mk_set
        ultimo_pop   = st.session_state.ultimo_pop
        
        # Cor dos nós no kNN
        node_color, node_size = [], []
        for n in G.nodes():
            if n == 1:
                node_color.append("#EF4444"); node_size.append(950)
            elif n in Mk_set:
                node_color.append("#22C55E"); node_size.append(850)
            elif ultimo_pop and n == ultimo_pop[2]:
                node_color.append("#60A5FA"); node_size.append(820)
            elif n in em_fila_set:
                node_color.append("#F59E0B"); node_size.append(780)
            elif n in OBJETOS:
                node_color.append("#6B7280"); node_size.append(700)
            else:
                node_color.append("#CBD5E1"); node_size.append(580)
                
        # Cor das arestas que ligam q aos predecessores na rede
        arestas_pred = {(1,2), (2,4), (4,5)}
        edge_color = []
        for u, v in G.edges():
            if (u,v) in arestas_pred or (v,u) in arestas_pred:
                edge_color.append("#A78BFA") # roxo para predecessores
            else:
                edge_color.append("#475569")
                
        fig, ax = plt.subplots(figsize=(7, 4.5))
        fig.patch.set_facecolor("#0F172A")
        ax.set_facecolor("#0F172A")
        
        nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size,
                               ax=ax, edgecolors="white", linewidths=1.5)
        nx.draw_networkx_edges(G, pos, width=2.2, alpha=0.85, ax=ax, edge_color=edge_color)
        nx.draw_networkx_labels(G, pos, font_size=11, font_color="white", font_weight="bold", ax=ax)
        
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,"weight"),
                                     font_size=9, font_color="#CBD5E1", ax=ax,
                                     bbox=dict(boxstyle="round,pad=0.2", fc="#1E293B", alpha=0.8))
        
        plt.axis("off"); plt.tight_layout()
        st.pyplot(fig); plt.close(fig)
        
        st.markdown(
            "<div style='font-size:0.8rem; text-align:center; color:#94A3B8'>"
            "<span style='color:#EF4444'>●</span> q=1 (consulta) &nbsp;|&nbsp; "
            "<span style='color:#60A5FA'>●</span> último desempilhado &nbsp;|&nbsp; "
            "<span style='color:#F59E0B'>●</span> na fila Q &nbsp;|&nbsp; "
            "<span style='color:#22C55E'>●</span> kNN confirmado &nbsp;|&nbsp; "
            "<span style='color:#6B7280'>●</span> objeto não visitado &nbsp;|&nbsp; "
            "<span style='color:#A78BFA'>▬</span> predecessores de q"
            "</div>",
            unsafe_allow_html=True
        )
        
        with st.expander("Indice CTLD pré-computado (entrada do algoritmo)"):
            st.markdown(
                "O índice armazena, para cada **predecessor c** de q, "
                "a lista dos objetos mais próximos *dentro do subgrafo local*, "
                "já em ordem crescente de distância."
            )
            cols_pred = st.columns(len(PRED_Q))
            for i, c in enumerate(PRED_Q):
                with cols_pred[i]:
                    st.markdown(f"**Predecessor c = {c}**")
                    st.markdown(f"lsd(c={c}, q=1) = **{DIST_PRED[c]}**")
                    for j, (lsd, o) in enumerate(INDICE[c]):
                        ativo = (st.session_state.ultimo_pop
                                 and st.session_state.ultimo_pop[1] == c
                                 and st.session_state.ultimo_pop[3] == j)
                        prefixo = "--> " if ativo else f"{j}. "
                        st.markdown(f"{prefixo} obj **{o}** — lsd={lsd} — dist_total={DIST_PRED[c]+lsd}")
                        
    # ── COLUNA 2 — PSEUDOCÓDIGO ──
    with col_algo:
        st.subheader("Pseudocódigo")
        st.caption("A linha destacada em amarelo é a que está sendo executada agora.")
        
        linha_ativa = st.session_state.linha_ativa
        
        def linha_html(num, texto, ativa):
            bg  = "#78350F" if ativa else "#1E293B"
            brd = "#FCD34D" if ativa else "#334155"
            ico = ">" if ativa else "&nbsp;&nbsp;"
            return (
                f"<div style='background:{bg};border-left:3px solid {brd};"
                f"padding:5px 8px;margin:2px 0;border-radius:4px;"
                f"font-family:monospace;font-size:0.85rem;color:#E2E8F0'>"
                f"<span style='color:#94A3B8;margin-right:6px'>{num}</span>"
                f"<span style='color:#FCD34D;margin-right:4px'>{ico}</span>"
                f"{texto}</div>"
            )
            
        html_pseudo = ""
        for num, txt in PSEUDOCODIGO:
            ativa = (linha_ativa is not None) and (num in linha_ativa or num == linha_ativa)
            html_pseudo += linha_html(num, txt, ativa)
        st.markdown(html_pseudo, unsafe_allow_html=True)
        
        st.divider()
        st.subheader("O que aconteceu?")
        if st.session_state.narrativa:
            cor_box = "#14532D" if not st.session_state.foi_duplicata else "#78350F"
            st.markdown(
                f"<div style='background:{cor_box};border-radius:8px;"
                f"padding:12px 14px;color:#E2E8F0;font-size:0.9rem;line-height:1.6'>"
                f"{st.session_state.narrativa}</div>",
                unsafe_allow_html=True
            )
        else:
            st.info("Inicialize o algoritmo para começar.")
            
        st.divider()
        st.subheader("Próximo passo")
        if st.session_state.Q and not st.session_state.terminado:
            prox = min(st.session_state.Q)
            d_p, c_p, o_p, idx_p = prox
            ja_em_mk = o_p in st.session_state.Mk_set
            acao_txt = (
                f"[!] **obj {o_p}** será desempilhado — já está em Mk (duplicata), será descartado."
                if ja_em_mk else
                f"[+] **obj {o_p}** será desempilhado e **adicionado** a Mk! (dist={d_p})"
            )
            st.markdown(
                f"<div style='background:#1E293B;border:1px dashed #475569;"
                f"border-radius:8px;padding:10px 12px;color:#CBD5E1;font-size:0.88rem'>"
                f">> {acao_txt}<br>"
                f"<span style='color:#94A3B8;font-size:0.8rem'>"
                f"dist={d_p} | via predecessor c={c_p}</span></div>",
                unsafe_allow_html=True
            )
        elif st.session_state.terminado:
            st.success("Algoritmo encerrado — não há próximo passo.")
        else:
            st.info("Inicialize o algoritmo para ver a pré-visualização.")

    # ── COLUNA 3 — FILA Q E RESULTADO ──
    with col_fila:
        st.subheader("Fila de Prioridade Q")
        st.caption("A heap garante que o menor dist sempre fica no topo. O topo [1o] é quem será desempilhado.")
        
        if not st.session_state.iniciado:
            st.info("Inicialize o algoritmo.")
        elif not st.session_state.Q:
            st.success("Fila vazia — algoritmo encerrou!")
        else:
            fila_ord = sorted(st.session_state.Q)
            d_max = max(d for d,*_ in fila_ord) or 1
            d_min = min(d for d,*_ in fila_ord)
            
            for i, (d, c, o, idx) in enumerate(fila_ord):
                is_top   = (i == 0)
                is_dup   = (o in st.session_state.Mk_set)
                bg       = "#16213E" if is_top else "#1E293B"
                borda    = ("#EF4444" if is_top else ("#F59E0B" if i==1 else "#334155"))
                icone    = "[1o]" if is_top else f"{i+1}º"
                tag_dup  = " <span style='color:#F87171;font-size:0.75rem'>[duplicata]</span>" if is_dup else ""
                
                pct = int((d / d_max) * 100)
                barra = (
                    f"<div style='background:#374151;border-radius:4px;height:6px;margin:6px 0'>"
                    f"<div style='background:#22C55E;width:{pct}%;height:6px;border-radius:4px'></div>"
                    f"</div>"
                )
                eq = f"lsd(c={c},q) + lsd(c={c},obj={o}) = {DIST_PRED[c]} + {d-DIST_PRED[c]} = <b>{d}</b>"
                
                st.markdown(
                    f"<div style='background:{bg};border:2px solid {borda};"
                    f"border-radius:10px;padding:10px 12px;margin-bottom:6px'>"
                    f"<div style='font-size:1.05rem;font-weight:bold;color:#F1F5F9'>"
                    f"{icone} &nbsp; Objeto <span style='color:#FCD34D'>{o}</span>{tag_dup}</div>"
                    f"<div style='color:#94A3B8;font-size:0.8rem;margin-top:3px'>"
                    f"via predecessor <b style='color:#C4B5FD'>c = {c}</b> &nbsp;|&nbsp; posição idx={idx}</div>"
                    f"<div style='color:#CBD5E1;font-size:0.82rem;margin-top:4px'>{eq}</div>"
                    f"{barra}"
                    f"</div>",
                    unsafe_allow_html=True
                )
                
        st.divider()
        st.subheader("Resultado Mk(q)")
        if st.session_state.Mk:
            prog_mk = len(st.session_state.Mk)
            st.progress(prog_mk / k)
            st.markdown(f"**{prog_mk} de {k} vizinhos encontrados**")
            for rank, obj in enumerate(st.session_state.Mk, 1):
                dist_obj = next(
                    (DIST_PRED[c] + lsd for c in PRED_Q
                     for lsd, o in INDICE[c] if o == obj), "?"
                )
                st.markdown(
                    f"<div style='background:#14532D;border-radius:8px;"
                    f"padding:8px 12px;margin-bottom:4px;color:#D1FAE5'>"
                    f"<b>{rank}º vizinho:</b> Objeto <b style='color:#FCD34D'>{obj}</b>"
                    f" &nbsp;—&nbsp; dist mínima ≈ {dist_obj}</div>",
                    unsafe_allow_html=True
                )
        else:
            st.info("Nenhum vizinho confirmado ainda.")
            
        st.divider()
        st.subheader("Histórico de Passos")
        if st.session_state.historico:
            container_hist = st.container(height=220)
            with container_hist:
                for entry in reversed(st.session_state.historico):
                    p_label = f"**Passo {entry['passo']}**" if entry['passo'] != "INIT" else "**Inicialização**"
                    st.markdown(p_label)
                    for l in entry["linhas"]:
                        st.markdown(f"&nbsp;&nbsp;&nbsp;{l}")
        else:
            st.caption("O histórico aparecerá aqui após inicializar.")
            
    # ── BANNER FINAL DO KNN ──
    if st.session_state.terminado:
        if len(st.session_state.Mk) >= k:
            st.balloons()
            st.success(
                f"**Busca concluída em {st.session_state.passo} passos!**  \n"
                f"Os **{k}** vizinhos mais próximos de q=1 são: **{st.session_state.Mk}**  \n"
                f"O algoritmo usou *parada precoce* — não precisou visitar todos os {len(OBJETOS)} objetos!"
            )
        else:
            st.warning(
                f"[!] Fila Q esvaziou antes de encontrar {k} vizinhos. "
                f"Resultado parcial: {st.session_state.Mk}. Tente um k menor."
            )