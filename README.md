#  Mission Control AI — AgroSat-1

# Integrantes
- Pedro Yoshikado Garcia — RM: 570449
- Pedro Andreassa Zamai RM:569318
- Thiago Maluf Hofmann RM: 569852

# O que o projeto faz
O Mission Control AI — AgroSat-1 é um sistema interativo de terminal projetado para monitorar telemetrias orbitais de satélites voltados ao agronegócio no Centro-Oeste brasileiro. O sistema combina uma camada lógica local em Python para validação matemática de limites críticos (como NDVI, temperatura e atitude) com o modelo de IA gpt-oss:120b via Ollama Cloud. A inteligência artificial atua de forma integrada em um loop contínuo de chatbot, interpretando anomalias complexas e gerando planos de mitigação em tempo real para os operadores em terra.

# Persona atendida
**Operador de Controle de Voo Espacial e Monitoramento Agrícola.** Justificativa: O sistema fornece um painel CLI de leitura rápida com alertas visuais imediatos e um chatbot direto para que o operador possa interagir, diagnosticar falhas na constelação e tomar decisões rápidas para evitar a perda de dados da safra em solo.

## Demonstração
- Menu
<img width="569" height="394" alt="image" src="https://github.com/user-attachments/assets/19e08dd5-5974-4711-aa42-4251e637ab99" />
- Cenário 01
<img width="1562" height="881" alt="image" src="https://github.com/user-attachments/assets/5ef955bc-3a13-413d-b6ec-a476dd02b57a" />
- Cenário 02
<img width="1534" height="612" alt="image" src="https://github.com/user-attachments/assets/22f23f21-8c1a-46a9-916c-6cce8f25fd11" />
- Cenário 03
<img width="1555" height="895" alt="image" src="https://github.com/user-attachments/assets/24b69ad1-86ec-4553-a001-da32ff3558ef" />
- Cenário 04
<img width="1541" height="935" alt="image" src="https://github.com/user-attachments/assets/c11bee4a-282a-4e0c-9fbb-a4ea47747dea" />
- Cenário 05
<img width="1534" height="886" alt="image" src="https://github.com/user-attachments/assets/5ef18622-57ad-47a2-a067-4a15e2e81e06" />
- Cenário 06
<img width="1552" height="905" alt="image" src="https://github.com/user-attachments/assets/cba68b4c-96e9-429e-896e-5ba6145ba9ca" />

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

## Proposta de Valor / Modelo de Negócio
1. Qual o problema real terrestre que esta missão resolve?
   - O AgroSat-1 resolve o problema da falta de previsibilidade e da resposta tardia a desastres climáticos e biológicos nas lavouras de larga escala no Centro-Oeste brasileiro. Ao cruzar telemetria orbital com o índice NDVI em solo, o sistema identifica precocemente o      estresse hídrico severo e anomalias na vegetação (como pragas ou secas severas). Isso permite que grandes produtores e cooperativas tomem ações de manejo agrícola e irrigação antes que a quebra de safra se materialize, protegendo a segurança alimentar e a               eficiência econômica do setor.
2. Quem paga pela solução?
   - O modelo de financiamento é **Híbrido**. A infraestrutura base de constelação e o desenvolvimento do software de controle de voo recebem fomento do setor público através de parcerias com o INPE e agências de desenvolvimento científico. Por outro lado, o acesso aos      relatórios analíticos de alta precisão e as chamadas da API de Inteligência Artificial para diagnóstico terrestre são custeados pelo setor privado, especificamente por grandes cooperativas agrícolas do Mato Grosso e tradings de commodities que necessitam de dados       preditivos de safra.
3. Métrica de impacto
   - Se o AgroSat-1 operar 100% saudável por um período consecutivo de 1 ano, o sistema garantirá o monitoramento contínuo de **5 milhões de hectares de lavoura** na região do Centro-Oeste. Com a mitigação precoce de pragas e a otimização do uso de insumos guiada pela       IA, projeta-se uma redução de perdas que equivale a evitar o desperdício de **120 mil toneladas de grãos** e uma eficiência operacional que mitiga a emissão indireta de **15 mil toneladas de CO₂** pelo uso inteligente de maquinário em terra.
4. Modelo de negócio
   - O modelo de negócio adotado é o de **DaaS (Data as a Service - Dado como Serviço)** combinado com assinatura corporativa. O software da CLI atua como a ponte de consumo para grandes players do agronegócio que assinam pacotes mensais para receber os dados brutos de      telemetria processados e os relatórios analíticos gerados pelo gpt-oss:120b. O faturamento é estruturado em níveis de latência e frequência de varredura orbital, garantindo receita recorrente para sustentar os custos de infraestrutura e tokens da Ollama Cloud.

## Vídeo de demonstração
https://youtu.be/uPmqgiGJGkw
