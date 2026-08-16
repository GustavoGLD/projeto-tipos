"""
Utilizar um tipo que não seja subclasse de Estado para phantom type dará erro
"""
from src.a2_datakinds.src_file import *

class NovoEstado: ...

if __name__ == "__main__":
    p1 = MaquinaDeVenda[int](0)
    p2 = MaquinaDeVenda[NovoEstado](0)