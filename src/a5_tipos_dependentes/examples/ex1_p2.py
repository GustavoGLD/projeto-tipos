"""
Correção
"""

from src.a5_tipos_dependentes.src_file import *

if __name__ == "__main__":
    valor_inputado = input()  # "F Gustavo" ou "J Microsoft", por exemplo

    tipo_inputado = valor_inputado[0]
    nome_inputado = valor_inputado[2:]

    match tipo_inputado:
        case "F":
            pessoa_fisica = criar_pessoa(tipo_inputado, nome_inputado)
            criar_cpf_para(pessoa_fisica)

        case "J":
            pessoa_juridica = criar_pessoa(tipo_inputado, nome_inputado)
            criar_cnpj_para(pessoa_juridica)

        case _:
            raise ValueError(f"Entrada inválida: {valor_inputado!r}")