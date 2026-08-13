"""
GARANTIR QUE O PARÂMETROS SOMÁVEIS SEJAM DO MESMO TIPO

Nosso exemplo abaixo se aproxima muito de
    soma :: Num a => a -> a -> a
    soma a b = a + b

pois `a` e `b` precisam ser somáveis entre si e a soma precisa continuar a pertencer ao mesmo tipo,
além de garantir que os parâmetros `a` e `b` sejam do mesmo tipo.
"""

from dataclasses import dataclass
from typing import Protocol, Self, TypeVar

class Somavel(Protocol):
    def __add__(self, other: Self) -> Self: ...

@dataclass
class Somar[T: Somavel]:
    a: T
    b: T
    def __call__(self) -> T:  # executar instância como uma função
        return self.a + self.b

if __name__ == "__main__":
    a1: int = Somar[int](10, 10)()            # isso dá certo
    a2: str = Somar[str]("strogo", "noff")()  # isso também dá certo
    b1: int = Somar[int](10, 10.0)()          # isso dá erro
    b2: str = Somar[str]("strogo", 9)()       # isso também dá erro
