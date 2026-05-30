import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def mostrar_boas_vindas(banner):
    console.print(banner, style="bold cyan")
    console.print("[bold white]A estabelecer ligação segura com a constelação AgroSat...[/bold white]\n")
    time.sleep(1)

def exibir_telemetria_e_alertas(dados, alertas):
    console.print("\n[bold yellow]📡 A RECEBER TELEMETRIA VIA DOWNLINK...[/bold yellow]")
    
    table = Table(title=f"Status Atual: {dados.get('nome_missao', 'Desconhecido')}", title_style="bold magenta")
    table.add_column("Parâmetro", style="cyan")
    table.add_column("Valor Atual", style="green")
    
    params = dados.get("parametros_atuais", {})
    table.add_row("Status Geral", str(dados.get("status_satelite")))
    table.add_row("Índice de Vegetação (NDVI)", str(params.get("ndvi_medio")))
    table.add_row("Temp. Payload Óptico", f"{params.get('temperatura_payload_optico_c')} °C")
    table.add_row("Armazenamento Ocupado", f"{params.get('armazenamento_ocupado_percentual')}%")
    table.add_row("Estabilidade Yaw", f"{params.get('estabilidade_atitude_yaw')}°")
    
    console.print(table)
    
    console.print("\n[bold red]⚠️  ANÁLISE DE LIMITES DO SISTEMA (HARD CODED):[/bold red]")
    for alerta in alertas:
        if "CRÍTICO" in alerta or "ALTO" in alerta:
            console.print(Panel(alerta, border_style="red", title="PERIGO"))
        elif "MÉDIO" in alerta:
            console.print(Panel(alerta, border_style="yellow", title="ATENÇÃO"))
        else:
            console.print(Panel(alerta, border_style="green", title="OK"))

def mostrar_status_ia(mensagem):
    """Helper para exibir o status da chamada da IA."""
    console.print(f"\n[bold green]🤖 {mensagem}[/bold green]")