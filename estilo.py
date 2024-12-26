from rich.console import Console

console = Console()

def exibir_em_negrito(texto, isArquivo=False):
    """
    Mostre o texto ou conteúdo de arquivo em negrito.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(f"[bold]{texto}[/bold]")

def exibir_em_italico(texto, isArquivo=False):
    """
    Mostre o texto ou conteúdo de arquivo em itálico.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(f"[italic]{texto}[/italic]")
