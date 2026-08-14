"""
mas agora, também, é possível incrementar o vetor sem perder a validação
"""
from src.a6_vetor_indexavel_seguro.src_file import add_last
if __name__ == "__main__":
    vetor1 = ("a", "b", "c", "d")
    vetor2 = add_last(vetor1, "e")
    vetor3 = add_last(vetor2, "f")
    elemento = vetor3[8]  # erro!