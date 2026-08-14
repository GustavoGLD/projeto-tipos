"""
HIGHER KINDED TYPES EM PYTHON ???

Queremos escrever uma função que faça:

    Maybe[int]       -> Maybe[str]
    IO[int]          -> IO[str]
    Result[int, E]   -> Result[str, E]

Ou seja:

    Container[int] -> Container[str]

sem precisar saber qual é o Container, desde que tenha o método `map()`.

para isso, usamos uma biblioteca chamada `returns`, que implementa Higher Kinded Types em Python.
"""

from typing import TypeVar

from returns.interfaces.mappable import MappableN
from returns.primitives.hkt import Kind1, kinded


Container = TypeVar("Container", bound=MappableN)

@kinded
def tornar_em_texto(
    container: Kind1[Container, int],
) -> Kind1[Container, str]:
    return container.map(str)

