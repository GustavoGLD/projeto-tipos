"""
DATAKINDS

No exercício da máquina de moedas, usamos DataKinds para limitar
quais tipos poderiam ser usados como estado da máquina.

Python não possui DataKinds, mas podemos chegar a uma ideia parecida
usando subclasses e limitando o tipo genérico a `Estado`.
"""

class Estado: ...
class Aguardando(Estado): ...
class InseriuMoeda(Estado): ...
class ProcessandoPedido(Estado): ...
class ServindoPedido(Estado): ...


class MaquinaDeVenda[EstadoAtual: Estado]:
    def __init__(self, vendas: int):
        self.vendas = vendas


if __name__ == "__main__":
    m1 = MaquinaDeVenda[ServindoPedido](0)
    m2 = MaquinaDeVenda[Aguardando](0)
    m3 = MaquinaDeVenda[InseriuMoeda](0)
    m4 = MaquinaDeVenda[ProcessandoPedido](0)
