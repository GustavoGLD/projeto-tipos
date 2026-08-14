"""
Estamos esperando um Container com Int, se passarmos um Container com outro tipo, o mypy vai reclamar.
"""

from src.higher_kinded_types.src_file import *
from returns.maybe import Some
from returns.io import IO

if __name__ == "__main__":
    a1 = tornar_em_texto(Some("42"))
    a2 = tornar_em_texto(IO(42.42))
