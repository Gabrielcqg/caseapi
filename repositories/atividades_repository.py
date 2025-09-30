import json
import os

DATA_FILE = "data/atividades.json"

def carregar_atividades():
    """Carrega atividades do arquivo JSON"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def salvar_atividades(atividades):
    """Salva atividades no arquivo JSON"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(atividades, f, indent=4)
