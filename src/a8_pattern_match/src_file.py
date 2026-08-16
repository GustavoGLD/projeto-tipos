"""
Árvore de Expressão

Modelamos a estrutura da expressão através de tipos.

Por exemplo, a expressão:
    10 + (2 * 3)

pode ser representada como:
    Soma(
        Constante(10),
        Mul(Constante(2), Constante(3))
    )

Cada operação (`Soma`, `Sub`, `Mul`, `Div`) recebe outras expressões, então montamos estruturas recursivas.

Usamos `match-case` para tratar cada forma possível e avaliar a expressão.

A ideia é deixar a própria estrutura dos tipos representar quais construções são válidas.
"""

from dataclasses import dataclass


class Expressao:
    pass


@dataclass(frozen=True)
class Constante(Expressao):
    valor: int


@dataclass(frozen=True)
class Soma(Expressao):
    esquerda: Expressao
    direita: Expressao


@dataclass(frozen=True)
class Sub(Expressao):
    esquerda: Expressao
    direita: Expressao


@dataclass(frozen=True)
class Mul(Expressao):
    esquerda: Expressao
    direita: Expressao


@dataclass(frozen=True)
class Div(Expressao):
    esquerda: Expressao
    direita: Expressao


def eval(expr: Expressao) -> int:
    match expr:
        case Constante(valor):
            return valor

        case Soma(esquerda, direita):
            return eval(esquerda) + eval(direita)

        case Sub(esquerda, direita):
            return eval(esquerda) - eval(direita)

        case Mul(esquerda, direita):
            return eval(esquerda) * eval(direita)

        case Div(esquerda, direita):
            return eval(esquerda) // eval(direita)

        case _:
            raise TypeError(f"Expressão inválida: {expr!r}")


if __name__ == "__main__":
    expr = Soma(
        Constante(10),
        Mul(Constante(2), Constante(3)),
    )

    print(eval(expr))
    # 16