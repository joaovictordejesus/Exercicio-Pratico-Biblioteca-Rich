from rich.console import Console
from rich.progress import track

console = Console()

def exibir_progresso(texto, isArquivo=False):
    """
    Simula uma barra de progresso ao exibir o texto ou conteúdo do arquivo
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    for step in track(range(len(texto)), description="Processando..."):
        pass
    console.print(texto, style="bold green")

def exibir_contagem(texto, isArquivo=False):
    """
    Mostra o texto ou conteúdo de arquivo com uma contagem regressiva simulada.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    for i in track(range(10, 0, -1), description="Contagem regressiva..."):
        pass
    console.print(texto, style="bold magenta")
