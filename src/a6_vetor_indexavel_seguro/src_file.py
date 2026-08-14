"""
Vetores indexáveis seguros!!!
Para isso, brincaremos com tuplas:
"""


"""
Nosso Vetor é uma tupla de vários (ou nenhum) elementos do tipo T.
"""
type Vetor[T] = tuple[*tuple[T, ...]]


"""
Add
basicamente, recebe uma tupla de Ts elementos e retorna Ts+T
"""
def add[*Ts, T](vetor: tuple[*Ts], elem: T) -> tuple[*Ts, T]:
    return (*vetor, elem)


"""
Remove
recebe uma tupla "Ts+T" e devolve apenas "Ts"
"""
def remove[*Ts, T](vetor: tuple[*Ts, T]) -> tuple[*Ts]:
    return vetor[:-1]


"""
Head
valida se a tupla contem ao menos um elemento de tipo genérico T, retornando T
"""
type VecNaoVazio[T] = tuple[
    T,                # um elemento é obrigatório
    *tuple[T, ...]    # após, pode vir nenhum ou mais elementos
]
def vhead[T](v: VecNaoVazio[T]) -> T:
    return v[0]


"""
Tail
recebe uma tupla T+Ts e retorna Ts
"""
def vtail[T, *Ts](v: tuple[T, *Ts]) -> tuple[*Ts]:
    return v[1:]