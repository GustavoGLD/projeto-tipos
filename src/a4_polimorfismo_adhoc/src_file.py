"""
Polimorfismo ad-hoc

Com polimorfismo ad-hoc, é possível definir comportamentos diferentes para uma mesma operação dependendo do tipo recebido.

Em Python, não temos sobrecarga tradicional de funções :(
Mas podemos fazer sobrecarga dos cabeçalhos das funções >:)

Usaremos o decorator `@overload`, da biblioteca `typing`, para isso.

Criaremos uma função `criar_documento(pessoa)` que:
    - Recebe PessoaFisica e retorna CPF
    - Recebe PessoaJuridica e retorna CNPJ

Ou seja, o tipo retornado pela função depende do tipo recebido como argumento.

O `mypy` consegue entender essas possibilidades e validar se estamos usando o resultado da função com o tipo correto.
"""

from dataclasses import dataclass
from typing import overload


@dataclass
class PessoaFisica:
    nome: str


@dataclass
class PessoaJuridica:
    nome: str


@dataclass
class CPF:
    valor: str


@dataclass
class CNPJ:
    valor: str


@overload
def criar_documento(pessoa: PessoaFisica) -> CPF:
    ...


@overload
def criar_documento(pessoa: PessoaJuridica) -> CNPJ:
    ...


def criar_documento(
    pessoa: PessoaFisica | PessoaJuridica,
) -> CPF | CNPJ:
    if isinstance(pessoa, PessoaFisica):
        return CPF("123")
    return CNPJ("456")

def usar_cpf(cpf: CPF) -> None:
    print(cpf.valor)

def usar_cnpj(cnpj: CNPJ) -> None:
    print(cnpj.valor)


if __name__ == "__main__":
    joao = PessoaFisica("joão")
    padaria = PessoaJuridica("padaria")

    joao_documento = criar_documento(joao)
    padaria_documento = criar_documento(padaria)

    usar_cpf(joao_documento)      # isso da certo
    usar_cnpj(padaria_documento)  # isso da certo, tambem

    usar_cpf(padaria_documento)   # isso da erro: padaria não tem CPF como documento
    usar_cnpj(joao_documento)     # isso da erro: joão não tem CNPJ como documento