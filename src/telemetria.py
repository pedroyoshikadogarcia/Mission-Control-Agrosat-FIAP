import json
import os

def ler_telemetria():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'data', 'cenarios.json')
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"erro": "Arquivo cenarios.json não encontrado. Cria o arquivo na pasta data!"}