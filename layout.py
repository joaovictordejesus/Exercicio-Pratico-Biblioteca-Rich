from rich.console import Console
from rich.text import Text

console = Console()

def exibir_caixa(texto, isArquivo=False):
    """
    Mosta o texto ou conteúdo de arquivo em um layout de caixa.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.rule("Texto em Caixa")
    console.print(Text(texto, style="bold blue"))

def exibir_colunas(texto, isArquivo=False):
    """
    Mostra o texto ou conteúdo de arquivo em formato de colunas.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(f"| {texto} |", justify="center", style="green")
