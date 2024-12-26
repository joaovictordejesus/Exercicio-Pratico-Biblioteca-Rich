from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_painel_simples(texto, isArquivo=False):
    """
    Mostra o texto ou conteúdo de arquivo em um painel simples.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(Panel(texto, title="Painel Simples", style="cyan"))

def exibir_painel_destaque(texto, isArquivo=False):
    """
    Mostra o texto ou conteúdo de arquivo em um painel com destaque.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(Panel(texto, title="Destaque", border_style="bold red"))
