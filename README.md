# Mission Control AI - AgroSat-1 
> **Global Solution 2026.1** > **Disciplina:** Prompt Engineering and Artificial Intelligence  
> **Curso:** Ciência da Computação - FIAP

---

##  Descrição do Projeto
O **Mission Control AI - AgroSat-1** é uma aplicação de terminal de alta performance (CLI) projetada para atuar como uma estação de monitoramento orbital automatizada. O sistema foca no monitoramento de lavouras e saúde de satélites no Centro-Oeste brasileiro (Mato Grosso).

A arquitetura do projeto combina duas camadas de inteligência:
1. **Lógica Determinística (Python Hard-Coded):** Validação matemática estrita de limites físicos (temperatura, atitude, armazenamento e NDVI) via telemetria.
2. **Inteligência Artificial Generativa:** Integração via API oficial do Ollama com o modelo de larga escala **`gpt-oss:120b`**, responsável por interpretar o contexto híbrido e gerar relatórios detalhados de mitigação e impacto agronômico.

---

##  Integrantes do Grupo
* **Pedro Yoshikado Garcia** - RM: 570449
* Pedro Andreassa Zamai - RM: 569318
* Thiago Maluf Hofmann - RM: 569852

---

##  Stack Técnica
* **Core:** Python 3.x
* **Interface CLI:** Rich Library (Renderização de tabelas, painéis dinâmicos de alerta e estilização avançada)
* **Engine de IA:** Ollama Client API (Modelo `gpt-oss:120b` na Ollama Cloud da FIAP)
* **Configuração:** Python-dotenv para isolamento de credenciais

---

##  Arquitetura do Projeto
```text
Mission-Control-Agrosat-FIAP/
├── data/
│   └── cenarios.json          # Banco de dados de simulação (6 cenários de telemetria)
├── prompts/
│   └── system_prompt.md       # Engenharia de Prompt (Persona de Engenheiro de Voo)
├── src/
│   ├── __init__.py
│   ├── alertas.py             # Camada lógica hard-coded (Ifs e Elses de validação)
│   ├── engine.py              # Integração e comunicação com a API Ollama Cloud
│   ├── telemetria.py          # Leitura e parsing dinâmico de cenários JSON
│   └── ui.py                  # Funções de renderização visual no terminal
├── assets/                    # Screenshots das simulações (Cenários 1 a 6)
├── .env                       # Chave de API (Protegido por .gitignore)
├── .gitignore
├── banner_ascii.py            # Elemento visual de boot do terminal
├── main.py                    # Ponto de entrada do sistema
└── requirements.txt           # Dependências do projeto
```

---

##  Cenários de Simulação Disponíveis
O sistema conta com um motor de injeção de falhas e estados orbitais com 6 cenários distintos para homologação da IA:

1. Crítico - Estresse Hídrico e Superaquecimento: Anomalia térmica no sensor e seca na safra.

2. Nominal - Safra Saudável e Hardware 100%: Satélite operando em condições ideais de saúde.

3. Emergência - Falha Crítica de Atitude: Desvio angular severo no eixo Yaw (Satélite capotando).

4. Alerta Agro - Praga ou Seca Extrema: Hardware saudável, mas NDVI crítico em solo.

5. Crítico de TI - Sobrecarga de Armazenamento: Estouro de buffer (100% de ocupação) e perda de dados.

6. Anomalia Ambiental - Tempestade Solar: Radiação ionizante forçando o Modo de Segurança (Safe Mode).

---

##  Instalação e Execução
1. Clonar o Repositório
  ```bash
  git clone https://github.com/PedroYoshikado/Mission-Control-Agrosat-FIAP.git
  cd Mission-Control-Agrosat-FIAP
  ```
2. Instalar Dependências
  ```bash
  pip install -r requirements.txt
  ```
3. Configurar as Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e insira a chave oficial fornecida para acesso à nuvem:
   ```bash
    OLLAMA_API_KEY=[Acesse https://ollama.com, criem uma conta gratuita e gerem uma API Key]
   ```
4. Executar o Painel
   ```bash
    python main.py
   ```

---

##  Resultados e Evidências
As capturas de tela demonstrando o comportamento do painel de controle e as tomadas de decisão da IA para cada um dos 6 estados orbitais encontram-se documentadas na pasta /assets.

---

##  Demonstração em Vídeo
Assista à defesa técnica do projeto e simulação ao vivo no YouTube:

- Video ainda sendo produzido
