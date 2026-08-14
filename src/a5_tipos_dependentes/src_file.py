"""
Tipos Dependentes!

É possível pegar strings recebidas em runtime, como `"F João"`, `"J Mercado"`, `"F Kelly"` e `"J Floricultura"`,
e fazer com que, após interpretar o primeiro caractere, o verificador de tipos saiba se o resultado é uma
`PessoaFisica` ou uma `PessoaJuridica`.

O valor `"F"` leva ao tipo `PessoaFisica`, enquanto `"J"` leva ao tipo `PessoaJuridica`.
"""

from dataclasses import dataclass
from typing import Literal, overload


class Pessoa:
    ...


@dataclass
class PessoaFisica(Pessoa):
    nome: str
    cpf: str | None = None


@dataclass
class PessoaJuridica(Pessoa):
    nome: str
    cnpj: str | None = None



# com o decorador "@overload" da biblioteca Typing, podemos escrever variações do cabeçalho da função para diferentes tipos

@overload
def criar_pessoa(
    input_tipo: Literal["F"],
    nome: str,
) -> PessoaFisica:
    ...


@overload
def criar_pessoa(
    input_tipo: Literal["J"],
    nome: str,
) -> PessoaJuridica:
    ...


def criar_pessoa(
    input_tipo: Literal["F", "J"],
    nome: str,
) -> PessoaFisica | PessoaJuridica:
    match input_tipo:
        case "F":
            return PessoaFisica(nome)
        case "J":
            return PessoaJuridica(nome)


def criar_cnpj_para(pj: PessoaJuridica) -> None:
    pj.cnpj = "1234567890"


def criar_cpf_para(pf: PessoaFisica) -> None:
    pf.cpf = "1234567890"

