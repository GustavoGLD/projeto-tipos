"""
PHANTOM TYPES

Usamos tipos fantasmas para representar, no próprio tipo de `Pedido`,
quais validações ele já passou.

Receber pedido -> Validar produto -> Validar estoque -> Validar endereço

O mypy ajuda a garantir que as etapas sejam executadas na ordem correta.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Pedido[*Validacoes]:
    produto: str
    quantidade: int
    endereco_entrega: str


class NaoValidado: ...
class ProdutoValido: ...
class EstoqueValido: ...
class EnderecoEntregaValido: ...


def receber_pedido() -> Pedido[NaoValidado]:
    return Pedido[NaoValidado]("frango", 3, "rua x")

def checar_produto(pedido: Pedido[NaoValidado]) -> Optional[Pedido[ProdutoValido]]:
    if pedido.produto in ["frango", "carne", "queijo"]:
        return Pedido(pedido.produto, pedido.quantidade, pedido.endereco_entrega)
    return None

def checar_estoque(pedido: Pedido[ProdutoValido]) -> Optional[Pedido[ProdutoValido, EstoqueValido]]:
    if pedido.quantidade <= 5:
        return Pedido(pedido.produto, pedido.quantidade, pedido.endereco_entrega)
    return None

def checar_endereco_entrega[P: Pedido](pedido: P) -> Optional[P]:
    if pedido.endereco_entrega in ["rua x", "rua y"]:
        return pedido
    return None

if __name__ == "__main__":
    pedido_nao_validado = Pedido[NaoValidado]("frango", 2, "rua x")
    pedido_produto_ok  = checar_produto(pedido_nao_validado)

    if not pedido_produto_ok:
        raise Exception("Produto inválido")

    pedido_estoque_ok = checar_estoque(pedido_produto_ok)

    if not pedido_estoque_ok:
        raise Exception("Estoque insuficiente")

    pedido_endereco_ok = checar_endereco_entrega(pedido_estoque_ok)