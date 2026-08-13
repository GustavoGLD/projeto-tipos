"""
Correção
"""
from src.a2_datakinds.src_file import *

class NovoEstado(Estado): ...

if __name__ == "__main__":
    m1 = MaquinaDeVenda[Aguardando](0)
    m2 = MaquinaDeVenda[NovoEstado](0)