def analisar_limites(dados):
    alertas = []
    
    if "parametros_atuais" not in dados:
        return ["Erro: Sem parâmetros de telemetria."]

    params = dados["parametros_atuais"]

    if params.get("ndvi_medio", 1.0) < 0.5:
        alertas.append("ALERTA AGRO [CRÍTICO]: Índice de vegetação (NDVI) abaixo do limite. Risco de quebra de safra por estresse hídrico.")
        
    if params.get("temperatura_payload_optico_c", 0) > 35:
        alertas.append("ALERTA HARDWARE [MÉDIO]: Sensor óptico superaquecendo (acima de 35°C). Imagens podem sofrer distorção.")
        
    if params.get("armazenamento_ocupado_percentual", 0) > 90:
        alertas.append("ALERTA SISTEMA [ALTO]: Buffer de memória 90% cheio. Necessário forçar downlink na próxima janela.")
        
    if not alertas:
        alertas.append("STATUS: Tudo verde. Satélite rodando liso e safra crescendo.")
        
    return alertas