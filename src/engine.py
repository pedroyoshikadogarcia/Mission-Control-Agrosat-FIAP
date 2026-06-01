import os
from ollama import Client
from dotenv import load_dotenv

load_dotenv()

historico_conversa = []

def ler_prompt_sistema():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'system_prompt.md')
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def inicializar_contexto_ia(dados_telemetria, alertas_codigo):
    global historico_conversa
    system_prompt = ler_prompt_sistema()
    
    historico_conversa = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""
        CONTEXTO OPERACIONAL DO SATÉLITE AGROSAT-1:
        Dados Brutos de Telemetria: {dados_telemetria}
        Alertas Lógicos do Sistema: {alertas_codigo}
        
        Considere estes dados como a realidade atual do satélite para responder às próximas perguntas do operador.
        """}
    ]

def enviar_para_ia(mensagem_usuario):
    global historico_conversa
    api_key = os.getenv("OLLAMA_API_KEY")
    
    if not api_key:
        return "[ERRO]: OLLAMA_API_KEY não configurada no arquivo .env."

    client = Client()
    historico_conversa.append({"role": "user", "content": mensagem_usuario})

    try:
        resposta = client.chat(
            model='gpt-oss:120b',
            messages=historico_conversa
        )
        texto_resposta = resposta['message']['content']
        historico_conversa.append({"role": "assistant", "content": texto_resposta})
        return texto_resposta
    except Exception as e:
        return f"[ERRO AO COMUNICAR COM OLLAMA CLOUD]: {str(e)}"