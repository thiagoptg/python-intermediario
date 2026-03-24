"""
Interface de linha de comando para o pacote personalizador.
"""

import argparse

from personalizador import layout, painel, progresso, estilo

modulos = {
    "1": layout,
    "layout": layout,
    "2": painel,
    "painel": painel,
    "3": progresso,
    "progresso": progresso,
    "4": estilo,
    "estilo": estilo,
}


def obter_funcoes(modulo):
    return {
        "1": list(filter(callable, vars(modulo).values()))[1],
        "2": list(filter(callable, vars(modulo).values()))[2],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Exibe texto formatado usando rich"
    )

    parser.add_argument(
        "entrada",
        help="Texto ou caminho do arquivo"
    )

    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Indica que a entrada é um arquivo"
    )

    parser.add_argument(
        "-m", "--modulo",
        required=True,
        help="Módulo: 1-layout, 2-painel, 3-progresso, 4-estilo"
    )

    parser.add_argument(
        "-f", "--funcao",
        required=True,
        help="Função: 1 ou 2 dentro do módulo"
    )

    args = parser.parse_args()

    modulo = modulos.get(args.modulo.lower())

    if not modulo:
        print("Módulo inválido")
        return

    funcoes = obter_funcoes(modulo)

    funcao = funcoes.get(args.funcao)

    if not funcao:
        print("Função inválida")
        return

    funcao(args.entrada, args.arquivo)


if __name__ == "__main__":
    main()