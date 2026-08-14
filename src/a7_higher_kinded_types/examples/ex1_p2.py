"""
Correção
"""
from src.higher_kinded_types.src_file import *
from returns.maybe import Some
from returns.io import IO
from returns.result import Success


if __name__ == "__main__":
    a1 = tornar_em_texto(Some(42))     # Some(42) -> Some("42")
    a2 = tornar_em_texto(IO(42))       # IO(42) -> IO("42")
    a3 = tornar_em_texto(Success(42))  # Success(42) -> Success("42")
