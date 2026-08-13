from typing import Protocol, Self


class Somavel(Protocol):
    def __add__(self, other: Self) -> Self:
        ...


class Ordenavel(Protocol):
    def __lt__(self, other: Self) -> bool:
        ...


def somar(a: Somavel, b: Somavel) -> Somavel:
    return a + b


def menor(a: Ordenavel, b: Ordenavel) -> Ordenavel:
    if a < b:
        return a
    return b


if __name__ == "__main__":
    print(somar(10, 20))
    print(somar("oi", " mundo"))

    print(menor(10, 20))
    print(menor("banana", "abacaxi"))

    somar(object(), object()) # dá erro, pois não possui __add__
    menor(object(), object()) # tambem dá erro, pois não possui __lt__ compatível

    somar("oi", 10) # deveria dar erro, mas passa. vamos arrumar no próximo exemplo