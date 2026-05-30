import os
from ollama import Client

def ler_prompt_sistema():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'system_prompt.md')
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def enviar_para_ia(dados_telemetria, alertas_codigo):
    client = Client(host='http://localhost:11434')
    system_prompt = ler_prompt_sistema()
    
    prompt_usuario = f"""
    ANALISAR TELEMETRIA ATUAL DO SATÉLITE:
    
    Dados de Órbita:
    {dados_telemetria}
    
    Alertas de Limites (Python hard-coded):
    {alertas_codigo}
    
    Por favor, gere o relatório completo da missão baseado estritamente nas seções do System Prompt.
    """

    try:
        resposta = client.generate(
            model='llama3',
            prompt=prompt_usuario,
            system=system_prompt
        )
        return resposta['response']
    except Exception as e:
        return f"[ERRO LOCAL]: Certifique-se de que o Ollama está aberto no PC. Detalhes: {str(e)}"