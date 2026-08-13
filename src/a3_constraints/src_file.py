"""
SIMULANDO CONSTRAINTS!

Com `Protocol`, podemos restringir um tipo pelo comportamento que ele precisa possuir.

Em Python, operadores normalmente são definidos por métodos especiais, os "dunder methods" (double underscore):
    +   -> __add__
    <   -> __lt__
    ==  -> __eq__
    *   -> __mul__
    /   -> __truediv__
    str -> __str__

Então podemos criar Protocols que exigem esses métodos.

Por exemplo:
    T: Somavel    -> T precisa possuir __add__, ou seja, suportar +
    T: Ordenavel  -> T precisa possuir __lt__, ou seja, suportar <

Não importa de qual classe o objeto seja ou herda, se ele possui os métodos exigidos pelo Protocol, o mypy aceita.
"""

from typing import Protocol, Self, TypeVar

class Somavel(Protocol):
    def __add__(self, other: Self) -> Self: ...

class Ordenavel(Protocol):
    def __lt__(self, other): ...

class Comparavel(Protocol):
    def __eq__(self, other): ...

class Imprimivel(Protocol):
    def __str__(self) -> str: ...

class Multiplicavel(Protocol):
    def __mul__(self, other): ...

class Divisivel(Protocol):
    def __truediv__(self, other): ...

