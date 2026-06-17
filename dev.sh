#!/usr/bin/env bash

# Encerrar imediatamente se qualquer comando falhar
set -e

# Obter o diretório onde este script está localizado
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "===================================================="
echo "🚀 Configurando ambiente — Zachary's Karate Club"
echo "===================================================="

# Verificar se a venv existe, se não, criar
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual Python (venv)..."
    python3 -m venv venv
fi

# Ativar a venv
echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar o pip e instalar dependências
echo "📥 Instalando/Atualizando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Ambiente pronto! Exemplos de uso:"
echo "   python3 scripts/gerar_dataset.py       # Gera os dados tratados"
echo "   python3 scripts/gerar_graficos.py      # Gera visualizações"
echo "   python3 scripts/run_benchmarks.py      # Benchmark dos algoritmos"
echo "   python3 scripts/analise_estrutural.py  # Análise Small-world, Lei de Potência, Robustez"
echo "   python3 scripts/executar_algoritmos.py # Demonstração de todos os algoritmos"
echo ""
echo "   Ou execute cada algoritmo individualmente:"
echo "   python3 algoritmos/bfs/bfs.py"
echo "   python3 algoritmos/dijkstra/dijkstra.py"
echo "   ..."
