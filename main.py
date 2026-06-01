import sys
import os
from banner_ascii import obter_banner
from src.telemetria import ler_telemetria, ler_todos_cenarios
from src.alertas import analisar_limites
from src.ui import mostrar_boas_vindas, exibir_telemetria_e_alertas, mostrar_status_ia, console
from src.engine import inicializar_contexto_ia, enviar_para_ia

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = obter_banner()
    console.print(banner, style="bold cyan")
    
    cenarios = ler_todos_cenarios()
    console.print("\n[bold white]Selecione o cenário de telemetria para carregar no Chatbot:[/bold white]")
    for c in cenarios:
        console.print(f" [bold green][{c['id']}][/bold green] - {c['nome_cenario']}")
        
    try:
        escolha = int(console.input("\nDigite o número do cenário: "))
    except ValueError:
        escolha = 1

    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_boas_vindas(banner)
    
    dados = ler_telemetria(escolha)
    if "erro" in dados:
        console.print(f"[bold red]{dados['erro']}[/bold red]")
        sys.exit(1)
        
    alertas_codigo = analisar_limites(dados)
    exibir_telemetria_e_alertas(dados, alertas_codigo)
    inicializar_contexto_ia(dados, alertas_codigo)
    
    console.print("\n[bold Box] ENGINE CONFIGURADA: gpt-oss:120b (Ollama Cloud) [/bold Box] [bold green]✓ PRONTO[/bold green]")
    console.print("[dim]Digite 'sair' ou 'exit' para acessar encerrar o painel de controle.[/dim]\n")
    
    while True:
        try:
            pergunta = console.input("[bold cyan]❯ [/bold cyan]")
            
            if pergunta.strip().lower() in ['sair', 'exit']:
                console.print("\n[bold yellow]Desconectando da constelação AgroSat. Transmissão encerrada.[/bold yellow]")
                break
                
            if not pergunta.strip():
                continue
                
            with console.status("[bold yellow]IA processando dados orbitais...", spinner="dots"):
                resposta_ia = enviar_para_ia(pergunta)
                
            console.print(f"\n[bold magenta]🤖 MISSION CONTROL AI:[/bold magenta]")
            console.print(f"{resposta_ia}\n")
            console.print("[dim]-----------------------------------------------------------------------[/dim]\n")
            
        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold yellow]Conexão abortada pelo operador. Finalizando...[/bold yellow]")
            break

if __name__ == "__main__":
    main()