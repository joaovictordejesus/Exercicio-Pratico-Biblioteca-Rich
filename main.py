import argparse
from personalizador import layout, painel, progresso, estilo

MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo,
}

FUNCOES = {
    "layout": ["exibir_caixa", "exibir_colunas"],
    "painel": ["exibir_painel_simples", "exibir_painel_destaque"],
    "progresso": ["exibir_progresso", "exibir_contagem"],
    "estilo": ["exibir_em_negrito", "exibir_em_italico"],
}

def main():
    parser = argparse.ArgumentParser(description="Programa de formatação usando Rich.")
    parser.add_argument("texto", help="Texto ou caminho para arquivo a ser processado.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo.")
    parser.add_argument("-m", "--modulo", choices=MODULOS.keys(), required=True, help="Escolhe o módulo.")
    parser.add_argument("-f", "--funcao", choices=sum(FUNCOES.values(), []), required=True, help="Escolhe a função.")
    
    args = parser.parse_args()

    modulo = MODULOS[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
