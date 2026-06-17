#!/usr/bin/env bash

# Encerrar imediatamente se qualquer comando falhar
set -e

# Obter o diretório onde este script está localizado
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "===================================================="
echo "🚀 Configurando ambiente do Simulador Zachary's Karate Club"
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

# Executar o simulador
echo "🎯 Iniciando o Streamlit..."
echo "Aguarde... O navegador abrirá automaticamente em instantes."
streamlit run scripts/script.py
