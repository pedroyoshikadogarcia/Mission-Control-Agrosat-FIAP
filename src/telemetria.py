import json
import os

def ler_todos_cenarios():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'data', 'cenarios.json')
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def ler_telemetria(id_cenario=1):
    cenarios = ler_todos_cenarios()
    for c in cenarios:
        if c.get("id") == id_cenario:
            return c
    return {"erro": f"Cenário com ID {id_cenario} não encontrado."}