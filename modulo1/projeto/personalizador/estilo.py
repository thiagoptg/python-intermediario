"""
Módulo responsável por estilos de texto.
"""

from rich.console import Console

console = Console()


def ler_texto(entrada, isArquivo):
    """Lê texto direto ou de arquivo."""
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada


def texto_colorido(entrada, isArquivo):
    """
    Exibe texto colorido.
    """
    texto = ler_texto(entrada, isArquivo)
    console.print(texto, style="bold green")


def texto_destacado(entrada, isArquivo):
    """
    Exibe texto com destaque.
    """
    texto = ler_texto(entrada, isArquivo)
    console.print(f"[reverse]{texto}[/reverse]")