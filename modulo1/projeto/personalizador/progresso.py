"""
Módulo responsável por barras de progresso.
"""

from rich.progress import track
from rich.console import Console
import time

console = Console()


def ler_texto(entrada, isArquivo):
    """Lê texto direto ou de arquivo."""
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada


def progresso_simples(entrada, isArquivo):
    """
    Exibe texto com barra de progresso simples.
    """
    texto = ler_texto(entrada, isArquivo)

    for _ in track(range(5), description="Processando..."):
        time.sleep(0.3)

    console.print(texto)


def progresso_lento(entrada, isArquivo):
    """
    Exibe texto com progresso mais lento.
    """
    texto = ler_texto(entrada, isArquivo)

    for _ in track(range(10), description="Carregando..."):
        time.sleep(0.2)

    console.print(texto)