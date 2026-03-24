"""
Módulo responsável por funcionalidades de layout usando rich.
"""

from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel

console = Console()


def ler_texto(entrada, isArquivo):
    """Lê texto direto ou de arquivo."""
    if isArquivo:
        with open(entrada, "r", encoding="utf-8") as f:
            return f.read()
    return entrada


def layout_duplo(entrada, isArquivo):
    """
    Exibe o texto dividido em dois painéis usando Layout.
    """
    texto = ler_texto(entrada, isArquivo)

    layout = Layout()
    layout.split_row(
        Layout(Panel(texto[:len(texto)//2], title="Parte 1")),
        Layout(Panel(texto[len(texto)//2:], title="Parte 2"))
    )

    console.print(layout)


def layout_simples(entrada, isArquivo):
    """
    Exibe o texto em um layout único centralizado.
    """
    texto = ler_texto(entrada, isArquivo)

    layout = Layout()
    layout.update(Panel(texto, title="Conteúdo"))

    console.print(layout)