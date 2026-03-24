"""
Módulo responsável por exibição em painéis.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()


def ler_texto(entrada, isArquivo):
    """Lê texto direto ou de arquivo."""
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada


def painel_simples(entrada, isArquivo):
    """
    Exibe texto dentro de um painel simples.
    """
    texto = ler_texto(entrada, isArquivo)
    console.print(Panel(texto, title="Painel"))


def painel_colorido(entrada, isArquivo):
    """
    Exibe texto dentro de um painel colorido.
    """
    texto = ler_texto(entrada, isArquivo)
    console.print(Panel(texto, title="Colorido", style="bold magenta"))