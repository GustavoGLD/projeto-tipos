"""
Demonstrando erros
"""
from src.a4_polimorfismo_adhoc.src_file import *

if __name__ == "__main__":
    joao = PessoaFisica("joão")
    padaria = PessoaJuridica("padaria")

    joao_documento = criar_documento(joao)
    padaria_documento = criar_documento(padaria)

    usar_cpf(padaria_documento)   # isso da erro: padaria não tem CPF como documento
    usar_cnpj(joao_documento)     # isso da erro: joão não tem CNPJ como documento