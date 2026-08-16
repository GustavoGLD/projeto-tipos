"""
Criando e usando documentos de uma pessoa física (joão) e uma pessoa jurídica (padaria)
"""

from src.a4_polimorfismo_adhoc.src_file import *

if __name__ == "__main__":
    joao = PessoaFisica("joão")
    padaria = PessoaJuridica("padaria")

    joao_documento = criar_documento(joao)
    padaria_documento = criar_documento(padaria)

    usar_cpf(joao_documento)      # isso da certo
    usar_cnpj(padaria_documento)  # isso da certo, tambem