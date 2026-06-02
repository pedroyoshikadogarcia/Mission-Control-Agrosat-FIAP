#  Mission Control AI — AgroSat-1

# Integrantes
- Pedro Yoshikado Garcia — RM: 570449
- Pedro Andreassa Zamai RM:569318
- Thiago Maluf Hofmann RM: 569852

# O que o projeto faz
O Mission Control AI — AgroSat-1 é um sistema interativo de terminal projetado para monitorar telemetrias orbitais de satélites voltados ao agronegócio no Centro-Oeste brasileiro. O sistema combina uma camada lógica local em Python para validação matemática de limites críticos (como NDVI, temperatura e atitude) com o modelo de IA gpt-oss:120b via Ollama Cloud. A inteligência artificial atua de forma integrada em um loop contínuo de chatbot, interpretando anomalias complexas e gerando planos de mitigação em tempo real para os operadores em terra.

# Persona atendida
**Operador de Controle de Voo Espacial e Monitoramento Agrícola.** Justificativa: O sistema fornece um painel CLI de leitura rápida com alertas visuais imediatos e um chatbot direto para que o operador possa interagir, diagnosticar falhas na constelação e tomar decisões rápidas para evitar a perda de dados da safra em solo.

# Tecnologias utilizadas
- Python 3.10+
- Ollama Cloud API (modelo gpt-oss:120b)
- Bibliotecas: ollama, python-dotenv, rich

## 📂 Estrutura do Projeto
```text
Mission-Control-Agrosat-FIAP/
├── data/
│   └── cenarios.json          # Banco de dados de simulação (6 cenários de telemetria)
├── prompts/
│   └── system_prompt.md       # Engenharia de Prompt (Persona do Engenheiro de Voo)
├── src/
│   ├── __init__.py
│   ├── alertas.py             # Camada lógica hard-coded (Regras de validação local)
│   ├── engine.py              # Integração e histórico de contexto com a Ollama Cloud
│   ├── telemetria.py          # Leitura e parsing dinâmico de cenários JSON
│   └── ui.py                  # Funções de renderização visual no terminal
├── assets/                    # Evidências de funcionamento (Cenários de teste)
├── .env                       # Chave privada da API (Protegido por .gitignore)
├── .env.example               # Exemplo de configuração de variáveis de ambiente
├── .gitignore                 # Filtro de arquivos para o Git
├── banner_ascii.py            # Elemento visual de boot do terminal
├── main.py                    # Ponto de entrada do sistema interativo (Chatbot loop)
└── requirements.txt           # Dependências fixadas do projeto
```

# Como executar
1. Clone o repositório:
```bash
   git clone [https://github.com/PedroYoshikado/Mission-Control-Agrosat-FIAP.git](https://github.com/PedroYoshikado/Mission-Control-Agrosat-FIAP.git)
   cd Mission-Control-Agrosat-FIAP
```
2. Crie ambiente virtual:
```bash
  python -m venv .venv && source .venv/bin/activate
```
(No Windows use: .venv\Scripts\activate)
3. Instale dependências:
```bash
  pip install -r requirements.txt
```
4. Crie arquivo .env na raiz com:
```bash
  OLLAMA_API_KEY=sua_chave_aquiOLLAMA_API_KEY=[Acesse https://ollama.com, criem uma conta gratuita e gerem uma API Key no painel de
configurações.]
```
5. Execute
```bash
  python main.py
```

## System Prompt
O prompt de sistema completo utilizado para configurar a persona do engenheiro de voo e as restrições de comportamento da IA encontra-se isolado no seguinte arquivo do repositório:
```
 prompts/system_prompt.md
```

## Cenários de teste demonstrados
1. Operação normal (Cenário 2): Satélite saudável, todos os parâmetros dentro do range ideal e biomassa da lavoura excelente.

2. Temperatura crítica (Cenário 1): Alerta local de superaquecimento do payload óptico combinado com estresse hídrico em terra.

3. Falha de Atitude / Perda de apontamento (Cenário 3): Desvio angular severo no eixo Yaw com satélite capotando em órbita.

4. Alerta Agro / Quebra de Safra (Cenário 4): Satélite 100% operacional, mas identificando anomalia severa (seca/praga) com NDVI crítico em solo.

5. Sobrecarga de TI (Cenário 5): Estouro de buffer com 100% de armazenamento ocupado e descarte de novos pacotes científicos.

6. Anomalia Ambiental (Cenário 6): Impacto de radiação por tempestade solar, forçando o satélite a entrar em Modo de Segurança (Safe Mode).

## Limitações conhecidas
- Falta de persistência de histórico em banco: O histórico de conversa do chatbot é mantido puramente na memória RAM (historico_conversa em formato de lista). Se o operador fechar o terminal ou o programa for encerrado, todo o contexto da conversa anterior é perdido.

- Ausência de telemetria em tempo real (Streaming): Os dados de telemetria não são recebidos via streaming real do espaço; o sistema trabalha com injeção estática de cenários pré-configurados através do arquivo cenarios.json.

- Dependência estrita de conexão síncrona: O chatbot não possui tratamento de timeout assíncrono ou modo offline. Caso a API da Ollama Cloud fique instável, a CLI trava o loop aguardando a resposta da rede.

## Vídeo de demonstração
https://youtu.be/uPmqgiGJGkw
