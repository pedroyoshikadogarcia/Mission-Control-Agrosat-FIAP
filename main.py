import sys
import os
from banner_ascii import obter_banner
from src.telemetria import ler_telemetria, ler_todos_cenarios
from src.alertas import analisar_limites
from src.ui import mostrar_boas_vindas, exibir_telemetria_e_alertas, mostrar_status_ia, console
from src.engine import enviar_para_ia

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = obter_banner()
    console.print(banner, style="bold cyan")
    
    cenarios = ler_todos_cenarios()
    console.print("\n[bold white]Selecione o cenário de telemetria para simular:[/bold white]")
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
    
    mostrar_status_ia("Conectando ao modelo gpt-oss:120b na Ollama Cloud... Analisando contexto...")
    
    with console.status("[bold yellow]IA interpretando telemetria e gerando plano de mitigação...", spinner="dots") as status:
        relatorio_ia = enviar_para_ia(dados, alertas_codigo)
        
    console.print("\n[bold cyan]=======================================================================[/bold cyan]")
    console.print("🤖 RELATÓRIO DO MISSION CONTROL AI (OLLAMA CLOUD)", style="bold magenta reverse")
    console.print("[bold cyan]=======================================================================[/bold cyan]\n")
    console.print(relatorio_ia)
    console.print("\n[bold cyan]=======================================================================[/bold cyan]")
    console.print("[bold green]Fim da transmissão de dados orbitais.[/bold green]\n")

if __name__ == "__main__":
    main()