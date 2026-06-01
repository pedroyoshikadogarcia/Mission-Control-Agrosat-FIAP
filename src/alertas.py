def analisar_limites(dados):
    alertas = []
    
    if "parametros_atuais" not in dados:
        return ["Erro: Sem parâmetros de telemetria."]

    params = dados["parametros_atuais"]
    status_geral = dados.get("status_satelite", "Operação Nominal")

    if status_geral == "Degradado":
        alertas.append("ALERTA HARDWARE [ALTO]: Subsistemas operando em modo degradado. Risco de perda de funções orbitais.")
    elif status_geral == "Modo de Segurança":
        alertas.append("ALERTA CRÍTICO [EMERGÊNCIA]: Satélite em SAFE MODE devido a anomalia ambiental externa.")

    ndvi = params.get("ndvi_medio", 1.0)
    if ndvi < 0.3:
        alertas.append("ALERTA AGRO [CRÍTICO]: NDVI extremamente baixo. Anomalia severa détectada em solo (seca severa ou praga).")
    elif ndvi < 0.5 and ndvi > 0.0:
        alertas.append("ALERTA AGRO [MÉDIO]: Índice de vegetação (NDVI) abaixo do limite ideal. Risco de estresse hídrico.")
        
    if params.get("temperatura_payload_optico_c", 0) > 35:
        alertas.append("ALERTA HARDWARE [MÉDIO]: Sensor óptico superaquecendo. Risco de distorção nas imagens térmicas.")

    if params.get("armazenamento_ocupado_percentual", 0) >= 100:
        alertas.append("ALERTA SISTEMA [CRÍTICO]: Memória 100% cheia. Dados científicos novos estão sendo DESCARTADOS.")
    elif params.get("armazenamento_ocupado_percentual", 0) > 90:
        alertas.append("ALERTA SISTEMA [ALTO]: Buffer de memória acima de 90%. Necessário forçar downlink urgente.")
        
    # Regra 5: Engenharia Espacial - Estabilidade de Atitude (Yaw)
    if params.get("estabilidade_atitude_yaw", 0) > 5.0:
        alertas.append("ALERTA CONTROLE [ALTO]: Desvio angular severo detectado no eixo Yaw. Perda de apontamento das câmeras.")
        
    if not alertas:
        alertas.append("STATUS: Tudo verde. Satélite rodando liso e safra crescendo.")
        
    return alertas